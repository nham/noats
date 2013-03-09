include_dir = build
title = 'notes on assorted things'

html:
	pandoc -s computability.md -t html5 -o computability.html \
		    --include-in-header $(include_dir)/header.html \
		    --include-before-body $(include_dir)/cover.html \
		    --include-after-body $(include_dir)/footer.html \
		    --title-prefix $(title) \
			--smart \
	        --mathjax

#	pandoc -s index.md -t html5 -o index.html \
			--smart
