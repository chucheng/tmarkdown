# tmarkdown.py

A template-based markdown plug-in. 
The program a simple script to help run markdown and merge its output to a template file.

Author: Chu-Cheng Hsieh  
Contact: chucheng <at> ucla <dot> edu


## Installation

	sudo cp tmarkdown.py /usr/bin/tmarkdown
	sudo chmod 755 /usr/bin/tmarkdown
	
## Usage
Usage: tmarkdown [options] <markdown file>

Options:
  -h, --help            show this help message and exit
  -t FILE, --template=FILE
                        assign a specific template filename
  -k STRING, --keyword=STRING
                        the keyword to be replaced in the template,the default
                        is: $content$
  -o, --output_to_html  write output to a file (replace md with html &
                        overwrite existed file.
  -i, --keep_indent     Counting # of space in front of the keyword and indent
                        each line in output.


## Pre-req
Make sure you have markdown ready.

The markdown should be able to run by issuing

	markdown <filename>
	
in your shell.


## Configuration
Or you may edit the variable **g_markdown_cmd** [Setting] section in the tmarkdown.py.

By default the keyword is $content$. You may customize it as well.


## Note

If not template file is assigned, the default one is the file with the same base filename and
the extension **.mdt**



## License

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.