#!/usr/bin/env python3
"""Extract the Escarcelle version and build date from an unpacked EscarcelleLinux binary.

The upstream binary is UPX-packed; run `upx -d` on it first.
Prints `VERSION=x.y.z` and `DATE=YYYY-MM-DD`, suitable for $GITHUB_OUTPUT.
"""

import re
import struct
import subprocess
import sys
from pathlib import Path

SYMBOL = "caisse/metier.version"
PT_LOAD = 1


def symbol_address(path: str, name: str) -> int:
    for line in subprocess.check_output(["nm", path], text=True).splitlines():
        parts = line.split(maxsplit=2)
        if len(parts) == 3 and parts[2] == name:
            return int(parts[0], 16)
    sys.exit(f"symbol {name!r} not found in {path}")


def va_to_offset(data: bytes, va: int) -> int:
    phoff, = struct.unpack_from("<Q", data, 0x20)
    phentsize, phnum = struct.unpack_from("<HH", data, 0x36)
    for i in range(phnum):
        p_type, _, p_offset, p_vaddr, _, p_filesz, _, _ = struct.unpack_from(
            "<IIQQQQQQ", data, phoff + i * phentsize
        )
        if p_type == PT_LOAD and p_vaddr <= va < p_vaddr + p_filesz:
            return va - p_vaddr + p_offset
    sys.exit(f"address {va:#x} not in any PT_LOAD segment")


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(f"usage: {sys.argv[0]} <unpacked-binary>")
    path = sys.argv[1]
    data = Path(path).read_bytes()

    # A Go string variable is a {ptr, len} header.
    ptr, length = struct.unpack_from("<QQ", data, va_to_offset(data, symbol_address(path, SYMBOL)))
    start = va_to_offset(data, ptr)
    version = data[start:start + length].decode()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        sys.exit(f"unexpected version string {version!r}")

    match = re.search(rb"vcs\.time=(\d{4}-\d{2}-\d{2})", data)
    if not match:
        sys.exit("vcs.time not found in build info")

    print(f"VERSION={version}")
    print(f"DATE={match.group(1).decode()}")


if __name__ == "__main__":
    main()
