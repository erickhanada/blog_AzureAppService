az login
az group create --name rg-blog --location brazilsouth

az appservice plan create \
  --name blog-plan \
  --resource-group rg-blog \
  --sku B1 \
  --is-linux

az webapp create \
  --resource-group rg-blog \
  --plan blog-plan \
  --name meu-blog-azure \
  --runtime "PYTHON|3.10"
