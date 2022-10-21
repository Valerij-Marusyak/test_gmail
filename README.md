Тестовое задание

Написать план тестирования(сценарий) формы login в gmail.
Покрыть сценарий с помощью selenium (java/gradle или python/pip) 
Сделать пуш в гит. В репозитории должен быть 	README.md,  в котором будут инструкции запуска. 

Сценарий

- Проверить вход с правильным адресом и паролем
- Проверить вход с неправильным паролем
- Проверить вход с неправильным адресом
- Проверить функциональность "Забыл пароль"
- Проверить функциональность "Забыл адрес"

Я реализовал несколько основных, на мой взгляд, тест-кейсов :). Есть еще много других, например:
- проверить предел количества неудачных попыток входа
- проверить возможность навигации с помощью клавиши "Табуляция"
- проверить работу в разных браузерах
- проверить невозможность логина с помощью нажатия на ссылку "Back" после логаута

К сожалению, времени на их выполнение просто не осталось :).

Чтобы проверить работу тестов, можно:
- Установить Python
- Установить PyCharm
- В PyCharm создать новый проект
- Скопировать в него папки page_object и tests со всем содержимым, а также файл requirements.txt
- Создать папку screenshots
- Открыть файл requirements.txt, нажать правую кнопку мыши и выбрать "Install All Packages"
- Создать конфигурацию запуска для файла test_login_pageobject.py
- Запустить его и возрадоваться :).
