# Deploying CF applications to SAP BTP

Deploying cf applications to SAP BTP is actually pretty easy. Thanks to the great work done by the SAP BTP the workflow is straight word. Check out the detailed blog post #todo (add blogpost link).
But if you want to run quick prototypes uploading the app as a zip file is note the best choice. Of course you can make use of the CF CLI and just push your app directly to SAP BTP to test you latest code or you can take it one step further and make use of Github Actions to automatically trigger the deployment as soon as you have committed your code

There a are a couple of things that we need to solve to get this setup. 

## Configure your deployment parameters with Github secrets

## Setup Github Actions

If you have your CF app in the root repository create a new workflow and edit the file as needed. This will trigger the deployment.

````yml
name: Deploy Python to Cloud Foundry
on:
  push: [ main ]
    
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name : CF PUSH
        uses: rangulvers/cf-push@main
        with:
          api:      ${{ secrets.CF_API }}
          org:      ${{ secrets.CF_ORG }}
          space:    ${{ secrets.CF_SPACE }}
          username: ${{ secrets.CF_USERNAME }}
          password: ${{ secrets.CF_PASSWORD }}
          manifest: manifest.yml
          validate: true
````

But what if you have multiple CF apps in one repository? Why would you do this? As you can see in this repository, this is what I'm doing. Since I want to offer a collection of coding examples around SAP and don't want to create repositories for each of them, I can just extend my coding and then push the new version of an app from the given directory. To achieve this we need to change the **yaml** file to only listen to the directory and to pass the appdir to the deploy process

````yml
name: Deploy Python to Cloud Foundry
on:
  push:
    paths:
    - 'BTP/cf_python/**' # Only listen to a specific folder
    
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name : CF PUSH
        uses: rangulvers/cf-push@main
        with:
          appdir:   './BTP/cf_python/testapp' # pass the app dir to the deploy process
          api:      ${{ secrets.CF_API }}
          org:      ${{ secrets.CF_ORG }}
          space:    ${{ secrets.CF_SPACE }}
          username: ${{ secrets.CF_USERNAME }}
          password: ${{ secrets.CF_PASSWORD }}
          manifest: manifest.yml
          validate: true

````