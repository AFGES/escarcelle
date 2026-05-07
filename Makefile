FLATPAK_ID = net.escarcelle.Cashdesk

.PHONY: build install run bundle clean

build:
	flatpak-builder --force-clean build-dir $(FLATPAK_ID).yaml

install:
	flatpak-builder --user --install --force-clean build-dir $(FLATPAK_ID).yaml

run:
	flatpak run $(FLATPAK_ID)

bundle: build
	flatpak build-update-repo repo
	flatpak build-bundle repo $(FLATPAK_ID).flatpak $(FLATPAK_ID)

clean:
	rm -rf build-dir .flatpak-builder repo $(FLATPAK_ID).flatpak
