# Приложение

Production пайплайн для простого Flask-приложения с экспортом метрик в Prometheus. Автоматическая сборка и публикация образа через GitHub Actions. Обновление Deployment в K8s при создании тега.

## Архитектура

> Проект опирается на [kubernetes](https://github.com/andrew-dibov/devops-kubernetes)

### Слой 1 : Приложение : Flask + Prometheus

| Функция | Описание |
| :-- | :-- |
| **Observability** | Экспорт метрик HTTP по `/metrics` |
| **Website** | `/` отображает приветственное сообщение из переменной окружения и `hostname` контейнера на который попал запрос |
| **Конфигурация** | Переменные окружения : `MESSAGE`, `HOST`, `PORT` |

### Слой 2 : Контейнеризация : Docker

Получение специального начального образа, установка зависимостей приложения, копирование кода и указание команды для его запуска.

### Слой 3 : CI/CD : GitHub Actions

| Workflow | Триггер | Действия |
| :-- | :-- | :-- |
| `build-push` | push в `main` или `workflow_dispatch` | Сборка образа -> публикация в реестре с тегами : `latest` и `github.sha` |
| `build-push-release` | push тега | `build-push` + обновление Deployment |

### Слой 4 : Автоматизация секретов : Bash

Обновление секретов репозитория и первый запуск `build-push` workflow :

| Ключ | Значение |
| :-- | :-- |
| `CONFIG` | Содержимое `~/.kube/config` в кодировке base64 |
| `REG_ID` | Container Registry ID |
| `SA_KEY` | Содержимое ключа сервисного аккаунта Terraform |

## Технологии и навыки

| Категория | Технологии/Инструменты | Навыки |
| :-- | :-- | :-- |
| **CI/CD** | GitHub Actions, Docker Buildx | Настройка пайплайнов сборки и деплоя, условное выполнение, управление секретами, кеширование слоев |
| **Containerization** | Docker, Container Registry | Сборка образов, мульти-тегирование, оптимизация кеша, отправка в реестр |
| **Orchestration** | Kubernetes | Обновление образов в Deployment, проверка статуса rollout|
| **Programming** | Python 3, Flask, Flask Exporter | Создание простого микросервиса с метриками, параметризация переменными окружения |
| **Security** | GitHub Secrets, Lockbox | Безопасное хранение и передача учетных данных, автоматическая выгрузка ключей из Lockbox |
| **Automation** | Bash, CLI инструменты | Автоматическая подготовка репозитория |

## Развертывание

```bash
sudo chmod +x bash/* && ./bash/init.sh
```
