import sys
import os, shutil, subprocess
from glob import glob

site_title = 'notes on assorted things'
include_dir = 'includes/'


def pandocConvert(fname):
    dothtml = fname[:fname.index('.')] + '.html'

    pandoc_call = ['pandoc', '-s', fname, '-t', 'html5', '-o', dothtml,
                          '--include-in-header', include_dir+'header.html',
                          '--include-before-body', include_dir+'cover.html',
                          '--include-after-body', include_dir+'footer.html',
                          '--mathjax', '--smart', '--title-prefix', site_title]

    p = subprocess.call(pandoc_call)

    return
    #return bytes.decode(p.communicate(bytes(source, 'UTF-8'))[0])


def isPage(fname):
    pages = ['.md', '.rst']
    return ('.' in fname) \
        and (fname[fname.index('.'):] in pages) \
        and fname != 'readme.md'

for fname in os.listdir('./'):
    if isPage(fname):
        pandocConvert(fname)



