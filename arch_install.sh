#!/bin/bash
# instalations scripte instalieren
pacman -Sy arch-install-scripts

echo "Bitte mounte alle gewünschten partitionen an der entsprechenden stelle(als root)"
echo "du benötigst(für uefi) folgende partitionen(mit gdisk): "
echo "/boot	ef00	512MB+"
echo "/	linux	rest"
echo "optional: swap (~ram), home"
echo "für bios noch eine ef02 2MB nicht einhängen"
#fake-root verzeicnis festlegen
read -p "Bitte gib das root verzeichnis des neuen Systems ein(startend von / ): " root
cd $root

#grundsystem + pakete instalieren instalieren
read -p "zusätzliche pakete, die instaliert werden sollen jetzt eingeben( space seperatet):" pkg
pacstrap $root -c -U base base-devel linux linux-firmware sudo nano vi vim dhcpcd bash-completion python $pkg

cd $root
#fstab erstellen + anzeigen
genfstab -Up $root > $root/etc/fstab
echo "tmpfs /var/cache/pacman/pkg tmpfs defaults  	0 0" >> $root/etc/fstab
cat $root/etc/fstab

read -p "hostname? " host
echo $host > etc/hostname

#localisation
echo LANG=en_US.UTF-8 > $root/etc/locale.conf
read -p "wenn du nicht englisch willst musst du $root/etc/locale.conf jetzt manuell bearbeiten.(bestätige mit enter)"
nano $root/etc/locale.gen

echo KEYMAP=de-latin1 > $root/etc/vconsole.conf
echo FONT=lat9w-16 >> $root/etc/vconsole.conf




arch-chroot $root locale-gen
arch-chroot $root ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime
arch-chroot $root mkinitcpio -p linux
arch-chroot $root passwd
read -p "instaliere jetzt grub, 64bit efi bootloader in $root/boot mit id $host, sollte das nicht gefallen, so beende das script jetzt(strg+C)"
arch-chroot $root pacman -Sy grub efibootmgr os-prober
arch-chroot $root grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=$host --recheck --debug --removable
arch-chroot $root grub-mkconfig -o /boot/grub/grub.cfg

#aushängen
echo "done, now umount, restart, enjoy!"
