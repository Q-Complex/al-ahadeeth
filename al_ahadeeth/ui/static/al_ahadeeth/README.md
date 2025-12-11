# UI Styles

Basic commands to get started.

First `cd` into dir:

```console
cd al_ahadeeth/ui/static/ui
```

To generate the styles:

```console
npm install
cd al_ahadeeth/ui/static/al_ahadeeth
npx @tailwindcss/cli -i ../static/al_ahadeeth/css/app.css -o ../static/al_ahadeeth/css/styles.css --cwd ../../templates -m -w
```

To format the templates:

```console
npx prettier -w ../../templates
```
