from stlitepack import pack, setup_github_pages
from stlitepack.pack import get_stlite_versions, list_files_in_folders

# We first check what stlite versions are available to choose from. This prints a
# message in the terminal.
get_stlite_versions()

files_to_link = [
        "scripts/arrival_chart.py", "scripts/label_results.py",
        "scripts/more_plot.py", "scripts/read_file.py",
        "scripts/scenarios.py", "scripts/setup.py"
        ]

files_to_link.extend(list_files_in_folders(folders=["img"], pattern=".png"))

files_to_link.extend(list_files_in_folders(folders=["txt", "data"]))

files_to_link.extend(["LICENSE", "CHANGES.md"])

pack(
    # When we're in the app folder, this is our entrypoint (main) file - the one we'd run if
    # we were previewing our streamlit app with the command `streamlit run`
    # In this case pages are structured using a pages folder, so they will automatically be
    # picked up and embedded
    app_file="Overview.py",
    requirements=["plotly==5.21.0", "matplotlib>=3.7.1",
                #   "pandas==2.0.2", "scipy==1.10.1", "numpy==1.25.0",
                  "pandas", "scipy", "numpy",
                  "simpy==4.1.1", "treat-sim==2.2.0"],
    use_raw_api=True,
    # stlitepack defaults to a slightly older version of stlite
    # We're going to request a version that's known to work particularly well (as versions either
    # side sometimes experience issues with either plotly plots displaying, or dataframes displaying)
    js_bundle_version="0.80.5",
    stylesheet_version="0.80.5",
    # Finally, we'll request to run a preview server so we can display the created app
    run_preview_server=True,
    prepend_github_path="bergam0t/stars-streamlit-example-stlitepack",
    extra_files_to_link=files_to_link
    )

# !! Note that because of the preview server being opened up,
# the next bit won't run until we close our preview server with CTRL + C !!

# We also want to create a workflow file to aid in deployment
setup_github_pages(
    # We want to deploy our site using github actions
    mode="gh-actions",
    # We are in the app subfolder, so we need to move up a level to the repository root
    # before we create the .github folder where our deployment workflow will sit
    # We didn't put our output in the docs folder when packing as there was already a different set
    # of documentation files in there - so we specify use_docs = False so that the created workflow
    # file knows to look at the root of the repository
    use_docs=True,
    # Finally, we want the .nojekyll files to be created automatically to ensure no post-processing
    # of our index.html file happens when it's uploaded to github pages
    create_nojekyll=True
    )
