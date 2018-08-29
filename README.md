# Maltego_Academia

#### Python transforms for exploring published papers and books

This is a set of transforms I have developed for exploring the academic literature. There is still quite some work to do, as of now it is still a beta version.

I am uploading it here to hopefully get some community interest, both from Maltego's community as from the academic research / data analysis community.

When completed, these transforms should allow you to explore a given academic field by graphically navigating through papers, authors (the two Maltego entities I have introduced), finding new papers published by the same author, or that share the same keywords, or that have been referenced by that paper. It will allow you to run a machine that follows a given author and notifies you when they've published a new paper, and automatically adds a new paper (node) to the graph. It eventually allow you to download the PDF and open it in your preferred program WITHOUT EVER LEAVING THE MALTEGO'S PLATFORM. 

In my mind, this should avoid you getting lost in loads of tabs, programs, and websites when you are doing research. It will help researchers being organised and focused on what exactly they are looking for, and what they know so far, by mapping it on a graph.

The idea is to harness Maltego's excellent platform to create graphs that can guide you in your research. 


Please let me know what you think, post your comments and questions, and if you would like to contribute that would be awsome! 

All of the trasforms are built using the TRX Python framework by Paterva. You can try them by adding this seed URL in the Transform Hub panel in Maltego.








Mainly I use public free APIs to run trasforms. By combining several services, the Maltego_Academia starts becoming quite versatile and powerful. Here is an up to date list of all the APIs used:

- [Crossref](https://www.crossref.org/)
- [Mendeley Reference Manager](https://www.mendeley.com/)
- [Google Scholar](https://scholar.google.com/), through the [Scholarly](https://pypi.org/project/scholarly/) Python module
- [BASE Bielefeld Academic Search Engine](https://www.base-search.net/about/en/)
- [Dimensions](https://www.dimensions.ai/)
- [Cermine PDF Content Extractor and Miner](http://cermine.ceon.pl/index.html)
- [Libgen Library Genesis](http://libgen.io)

