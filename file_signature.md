# File Magic Numbers

Magic numbers are the first bits of a file which uniquely identify the type of file. This makes programming easier because complicated file structures need not be searched in order to identify the file type.

For example, a jpeg file starts with ffd8 ffe0 0010 4a46 4946 0001 0101 0047 ......JFIF.....G
ffd8 shows that it's a JPEG file, and ffe0 identify a JFIF type structure. There is an ascii encoding of "JFIF" which comes after a length code, but that is not necessary in order to identify the file. The first 4 bytes do that uniquely.

This gives an ongoing list of file-type magic numbers.

## Image Files

<table border=1>
<tr>
  <th>File type</th>  <th>Typical <br>extension</th>  
  <th>Hex digits<br>xx = variable</th>
  <th>Ascii digits<br>. = not an ascii char</th>
</tr>

<tr>
  <td>Bitmap format</td>
  <td>.bmp</td>
  <td>42 4d</td>
  <td>BM</td>
</tr>

<tr>
  <td>FITS format</td>
  <td>.fits</td>
  <td>53 49 4d 50 4c 45</td>
  <td>SIMPLE</td>
</tr>

<tr>
  <td>GIF format</td>
  <td>.gif</td>
  <td>47 49 46 38</td>
  <td>GIF8</td>
<tr>

<tr>
  <td>Graphics Kernel System</td>
  <td>.gks</td>
  <td>47 4b 53 4d</td>
  <td>GKSM</td>
</tr>

<tr>
  <td>IRIS rgb format</td>
  <td>.rgb</td>
  <td>01 da</td>
  <td>..</td>
</tr>

<tr>
  <td>ITC (CMU WM) format</td>
  <td>.itc</td>
  <td>f1 00 40 bb</td>
  <td>....</td>
</tr>

<tr>
  <td>JPEG File Interchange Format</td>
  <td>.jpg</td>
  <td>ff d8 ff e0</td>
  <td>....</td>
</tr>

<tr>
  <td>NIFF (Navy TIFF)</td>
  <td>.nif</td>
  <td>49 49 4e 31</td>
  <td>IIN1</td>
</tr>

<tr>
  <td>PM format</td>
  <td>.pm</td>
  <td>56 49 45 57</td>
  <td>VIEW</td>
</tr>

<tr>
  <td>PNG format</td>
  <td>.png</td>
  <td>89 50 4e 47</td>
  <td>.PNG</td>
</tr>

<tr>
  <td>Postscript format</td>
  <td>.[e]ps</td>
  <td>25 21</td>
  <td>%!</td>
</tr>

<tr>
  <td>Sun Rasterfile</td>
  <td>.ras</td>
  <td>59 a6 6a 95</td>
  <td>Y.j.</td>
</tr>

<tr>
  <td>Targa format</td>
  <td>.tga</td>
  <td>xx xx xx</td>
  <td>...</td>
</tr>

<tr>
  <td>TIFF format (Motorola - big endian) </td>
  <td>.tif</td>
  <td>4d 4d 00 2a</td>
  <td>MM.*</td>
</tr>

<tr>
  <td>TIFF format (Intel - little endian) </td>
  <td>.tif</td>
  <td>49 49 2a 00</td>
  <td>II*.</td>
</tr>

<tr>
  <td>X11 Bitmap format</td>
  <td>.xbm</td>
  <td>xx xx</td>
  <td></td>
</tr>

<tr>
  <td>XCF Gimp file structure</td>
  <td>.xcf</td>
  <td>67 69 6d 70 20 78 63 66 20 76</td>
  <td>gimp xcf</td>
</tr>

<tr>
  <td>Xfig format</td>
  <td>.fig</td>
  <td>23 46 49 47</td>
  <td>#FIG</td>
</tr>

<tr>
  <td>XPM format</td>
  <td>.xpm</td>
  <td>2f 2a 20 58 50 4d 20 2a 2f</td>
  <td>/* XPM */</td>
</tr>

</table>

## Compressed files

<table border=1>
<tr>
  <th>File type</th>  <th>Typical <br>extension</th>  
  <th>Hex digits<br>xx = variable</th>
  <th>Ascii digits<br>. = not an ascii char</th>
</tr>

<tr>
  <td>Bzip</td>
  <td>.bz</td>
  <td>42 5a</td>
  <td>BZ</td>
</tr>

<tr>
  <td>Compress</td>
  <td>.Z</td>
  <td>1f 9d</td>
  <td>..</td>
</tr>

<tr>
  <td>gzip format</td>
  <td>.gz</td>
  <td>1f 8b</td>
  <td>..</td>
</tr>

<tr>
  <td>pkzip format</td>
  <td>.zip</td>
  <td>50 4b 03 04</td>
  <td>PK..</td>
</tr>

</table>

## Archive files

<table border=1>
<tr>
  <th>File type</th>  <th>Typical <br>extension</th>  
  <th>Hex digits<br>xx = variable</th>
  <th>Ascii digits<br>. = not an ascii char</th>
</tr>

<tr>
  <td>TAR (pre-POSIX)</td>
  <td>.tar</td>
  <td>xx xx</td>
  <td>(a filename)</td>
</tr>

<tr>
  <td>TAR (POSIX)</td>
  <td>.tar</td>
  <td>75 73 74 61 72</td>
  <td>ustar (offset by 257 bytes)</td>
</tr>

</table>

## Excecutable files

<table border=1>
<tr>
  <th>File type</th>  <th>Typical <br>extension</th>  
  <th>Hex digits<br>xx = variable</th>
  <th>Ascii digits<br>. = not an ascii char</th>
</tr>

<tr>
  <td>MS-DOS, OS/2 or MS Windows</td>
  <td>&nbsp;</td>
  <td>4d 5a</td>
  <td>MZ</td>
</tr>

<tr>
  <td>Unix elf</td>
  <td>&nbsp;</td>
  <td>7f 45 4c 46</td>
  <td>.ELF</td>
</tr>
</table>

## Miscellaneous files

<table border=1>
<tr>
  <th>File type</th>  <th>Typical <br>extension</th>  
  <th>Hex digits<br>xx = variable</th>
  <th>Ascii digits<br>. = not an ascii char</th>
</tr>

<tr>
  <td>pgp public ring</td>
  <td>&nbsp;</td>
  <td>99 00</td>
  <td>..</td>
</tr>

<tr>
  <td>pgp security ring</td>
  <td>&nbsp;</td>
  <td>95 01</td>
  <td>..</td>
</tr>

<tr>
  <td>pgp security ring</td>
  <td>&nbsp;</td>
  <td>95 00</td>
  <td>..</td>
</tr>

<tr>
  <td>pgp encrypted data</td>
  <td>&nbsp;</td>
  <td>a6 00</td>
  <td>&#166;.</td>
</tr>

</table>



