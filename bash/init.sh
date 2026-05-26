cat ~/.kube/config | base64 -w 0 | gh secret set CONFIG
YC_CLI_INITIALIZATION_SILENCE=true yc container registry list --format json | jq -r '.[] | select(.name == "cr--application") | .id' | gh secret set REG_ID
YC_CLI_INITIALIZATION_SILENCE=true yc lockbox payload get --name "ls--terraform-key" --key "ls__terraform_key" | gh secret set SA_KEY

gh workflow run build-push.yml --ref main
