```bash
gh secret set CONFIG # cat ~/.kube/config | base64 -w 0
gh secret set REG_ID # yc container registry list
gh secret set SA_KEY # yc lockbox payload get --name "ls--terraform-key" --key "ls__terraform_key"

gh workflow list
gh workflow run build-push --ref main
gh run list --workflow="build-push.yml"
```

Обновлять сразу в Ansible при пересоздании кластера?