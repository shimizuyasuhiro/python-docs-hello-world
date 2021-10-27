---
page_type: sample
description: "A minimal sample app that can be used to demonstrate deploying Bottle ~~Flask~~ apps to Azure App Service on Linux."
languages:
- python
products:
- azure
- azure-app-service
---

# Azure App Service (Linux) で bottle を動かす

前は Bottle のチュートリアルやテンプレレポジトリもあったようなのだが、公式採用しなくなったからとかなのか、
消滅しているようだったので、公式テンプレートの Flask 版をフォークして Bottle 用に書き換えてみる。

## ポイント

1. requirements.txt を Bottle を利用するように変更する

2. app.py の Flask 記述部分を bottle の記述に変更する
   - サンプルコードなどでは最後に`run()`を呼び出すことが多いが`app=default_app()`にする

> # Python Bottle ~~Flask~~ sample for Azure App Service (Linux)
>
> This is a minimal Bottle ~~Flask~~ app that can be deployed to Azure App Service on Linux.
>
> For instructions on running and deploying the code, see [Quickstart: Create a Python app in Azure App Service on Linux](https://docs.microsoft.com/azure/app-service/quickstart-python).
>
> ## Contributing
>
> This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.> microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
