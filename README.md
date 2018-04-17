# LibreScan

## Comunidad
- Hemos creado un bot de telegram para mantener a todos informados sobre los avances del proyecto, agrega el bot `@Librescan_bot` para recibir notificaciones. Creditos a nuestro amigo [Lupa18](https://github.com/lupa18) por nuestro bot de telegram! 

## Instalación

- Instalar dependencias que serán utilizadas:

		# apt-get install python3-pip lua5.2 liblua5.2 git-svn libusb-dev python3 python-dev libjpeg8 libffi-dev libturbojpeg1-dev

		# pip3 install pyYAML bottle pyjade jinja2 polib cffi pexpect

		# pip3 install jpegtran-cffi==0.5.2

--------------------------------------------------------------------------------------------

- Instalar tesseract-ocr para el reconocimiento de texto:

		# apt-get install tesseract-ocr

	Nota: Para más idiomas se instala de esta forma (Ejemplo con español): 

		# apt-get install tesseract-ocr-spa (Para Español) 

--------------------------------------------------------------------------------------------

- Instalar scantailor para el procesamiento de las fotos:

		# apt-get install scantailor
	
	Nota: Si no se encuentra en los repositorios agregar este a /etc/apt/sources.list: 

		- deb http://http.debian.net/debian wheezy-backports main

		Posteriormente hacer un # apt-get update

--------------------------------------------------------------------------------------------

- Instalar pdfbeads para generar pdfs a partir de tifs+hocr:

		# apt-get install ruby ruby-dev ruby-rmagick 
		# gem install iconv pdfbeads


--------------------------------------------------------------------------------------------
- En cuanto a las cámaras hay que instalar el CHDKPTP en el sistema.

		$ git svn clone http://subversion.assembla.com/svn/chdkptp/trunk chdkptp

		$ cd chdkptp

    -- nota: al 01.02.2015 Checked out HEAD:
       http://subversion.assembla.com/svn/chdkptp/trunk r694

		$ mv config-sample-linux.mk config.mk

		$ make

		# mkdir /usr/bin/chdkptp

		# cp chdkptp-sample.sh /usr/bin/chdkptp/chdkptp

      -- nota: chdkptp-sample.sh está en la dirección donde se descargó el chdkptp.

		# nano /usr/bin/chdkptp/chdkptp

Modificar la línea que dice

    #CHDKPTP_DIR=/path/to/chdkptp

por: 
	
	CHDKPTP_DIR=<FolderClonado>/chdkptp (Y guardamos los cambios)

nota: <FolderClonado>/chdkptp es la dirección donde se haya clonado el chdkptp (en el primer paso de esta sección). 

		# ln -s /usr/bin/chdkptp/chdkptp /bin

--------------------------------------------------------------------------------------------
- Es necesario tener CHDK instalado en las cámaras. (En caso de no tenerlo se puede seguir esta guía. Se recomienda usar el método "a"): 
https://github.com/LabExperimental-SIUA/ilt/wiki/Instalaci%C3%B3n-de-CHDK 

- Para reconocer cuál cámara es la derecha y cuál es la izquierda hacemos uso de un archivo 'orientation.txt', que se encuentra almacenado la raíz de la tarjeta SD de cada cámara. Por ahora este proceso se debe hacer manualmente, introduciendo la SD en la computadora y creando el archivo manualmente. Pasos:
	
	1. Asegurarse que la SD esté desbloqueada.
	2. Para la cámara que desea usar al lado izquierdo, crear un archivo orientation.txt que tenga la palabra 'left' (sin comillas) como contenido.
	3. Para la cámara que desea usar al lado derecho, crear un archivo orientation.txt que tenga la palabra 'right' (sin comillas) como contenido.



Nota: Estamos trabajando en automatizar este proceso, de modo que se el usuario conecte las cámaras y decida la orientación sin crear el archivo manualmente.

--------------------------------------------------------------------------------------------
- Una vez instaladas todas las dependencias, procedemos a clonar el repositorio de LibreScan.

		$ git clone https://github.com/LabExperimental-SIUA/LibreScan.git

- Nos metemos a la carpeta clonada, y al código fuente.

		$ cd LibreScan/src

- Corremos el setup para la creación de carpetas y archivos de configuración.

		$ python3.4 setup.py
		
- Para ejecutar la aplicación web

		$ python3.4 main.py web

- Por último, abrimos el navegador en http://0.0.0.0:8180
