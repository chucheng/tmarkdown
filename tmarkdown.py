#!/usr/bin/python
__author__ = 'chucheng'
__contact__ = 'chucheng <at> ucla <dot> edu'

"""
"tmarkdown" is a simple script to help run markdown and merge its output to a template file.

Pre-requistie:
  you should already install markdown and the markdown must be triggered by
  calling the command "markdown <filename>".

  Or you may modify the setting below and assign the right command.


The extension of a markdown template by default is mdt

This script will allow you to embed the output of your markdown
to a <head></head> and other non-supported html tag.


License:
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
"""

#Settings

#command that runs markdown
g_markdown_cmd = 'markdown'
g_keyword_in_template = '$content$'

import sys
import os
import commands
from optparse import OptionParser

if __name__ == '__main__':
    usage = "usage: %prog [options] <markdown file>"
    parser = OptionParser(usage)
    parser.add_option("-t", "--template", dest="template_filename",
                      help="assign a specific template filename", metavar="FILE")
    parser.add_option("-k", "--keyword", dest="template_keyword",
                      help="the keyword to be replaced in the template," +
                           "the default is: " + g_keyword_in_template,
                      metavar="STRING",
                      default=g_keyword_in_template)
    parser.add_option("-o", "--output_to_html", dest="output_to_html", default=False,
                      action='store_true',
                      help="write output to a file (replace md with html & overwrite existed file.")

    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
        sys.exit()

    #test markdown command
    status, md_output = commands.getstatusoutput(
        g_markdown_cmd + " ''")
    if status != 0:
        print "Error: the markdown command does not exist. Did you install markdown (lowercase)?"
        sys.exit()

    #assign default mdt if necessary
    if not options.template_filename:
        target_filename = args[0]
        base_filename = os.path.splitext(
            os.path.basename(target_filename)
        )[0] #get the basename without extension
        target_dir = os.path.dirname(target_filename)
        options.template_filename = target_dir + base_filename + ".mdt" #markdown template

    #make sure mdt exists
    if not os.path.exists(options.template_filename):
        print "Error: cannot find the template file: " + options.template_filename
        parser.print_help()
        sys.exit()

    find_keyword_before = False

    lines_to_write = ""

    with open(options.template_filename, 'r') as tf:
        for line in tf:
            if options.template_keyword in line:
                if find_keyword_before:
                    print "\n Error: the keyword exists more than once in your template file."
                    print "Check this keyword: " + options.template_keyword

                #find the keyword that need to be replaced
                status, md_output = commands.getstatusoutput(
                    g_markdown_cmd + " " + args[0])

                with open(args[0]) as markdown_target_fn:
                    if options.output_to_html: #write to file
                        lines_to_write += (md_output + "\n")
                    else: #display in stdout
                        print md_output

                    find_keyword_before = True
            else:
                if options.output_to_html:
                    lines_to_write += line
                else:
                    sys.stdout.write(line)

    # Write to html when -o is provided
    if options.output_to_html:
        target_filename = args[0]
        base_filename = os.path.splitext(
            os.path.basename(target_filename)
        )[0] #get the basename without extension
        target_dir = os.path.dirname(target_filename)
        output_filename = target_dir + base_filename + ".html" #output file name
        with open(output_filename, 'w') as of:
            of.write(lines_to_write)

