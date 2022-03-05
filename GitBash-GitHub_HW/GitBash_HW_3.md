1. ###### *На локальном репозитории сделать ветки для:*
    - ###### **Postman - `git branch Postman`**
    - ###### **Jmeter - `git branch Jmeter`**
    - ###### **CheckLists - `git branch CheckLists`**
    - ###### **Bug Reports - `git branch BagReports`**
    - ###### **SQL - `git branch SQL`**
    - ###### **Charles - `git branch Charles`**
    - ###### **Mobile testing - `git branch Mobile testing`**

2. ###### *Запушить все ветки на внешний репозиторий* \- **`git push -u origin Postman Jmeter CheckLists BugReports SQL Charles Mobile_testing`**

3. ###### *В ветке Bug Reports сделать текстовый документ со структурой баг репорта:*
    - ###### **`git checkout BugReports`**
    - ###### **`touch file_1.txt`**
    - ###### **`vim file_1.txt`**

4. ###### *Запушить структуру багрепорта на внешний репозиторий:*
    - ###### **`git add . && git commit -m "new file"`**
    - ###### **`git push`**

5. ###### *Вмержить ветку Bug Reports в Main*
    - ###### **`git checkout main`**
	- ###### **`git merge BugReports`**

6. ###### *Запушить main на внешний репозиторий* - **`git push`**

7. ###### *В ветке CheckLists набросать структуру чек листа:*
    - ###### **`git checkout CheckLists`**
	- ###### **`touch file_2.txt`**
    - ###### **`vim file_2.txt`**

8. ###### *Запушить структуру на внешний репозиторий:*
    - ###### **`git add . && git commit -m "new file_2"`**
	- ###### **`git push`**

9. ###### *На внешнем репозитории сделать Pull Request ветки CheckLists в main:*
    - ###### **Нажать `Compare & pull request`**
    - ###### **`Create pull request`**
    - ###### **`Merge pull request`**
    - ###### **`Confirm merge`**

10. ###### *Синхронизировать Внешнюю и Локальную ветки Main:*
    - ###### **`git checkout main`**
    - ###### **`git pull`**
