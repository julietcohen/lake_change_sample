# lake_change_sample
Learning PDG workflow with parsl by processing sample data for lake change in the Arctic.

### File Descriptions:
**stage_rasterize.ipynb:** initial exploration of the dataset sample, as well as the staging and rasterization steps\
**make_3d_tiles.ipynb:** initial attempt at the next steps in the workflow following staging and rasterization, but I abandoned this document in favor of starting a cleaner one from scratch to more clearly follow the PDG workflow from start to finish\
**workflow.ipynb:** most comprehensive document with documentation for my own knowledge\
**parsl.ipynb:** first run of `parsl` workflow (all at once, not chunked by step)\
**parsl_chunks.ipynb:** running through `parsl` workflow in steps (working on parsing this code between parsl and kubernetes, and setting up the `HighThroughputExecutor`)


I chose to not push the data folders to GitHub, but they can be found in datateam: `/home/jcohen/lake_change_sample/`
