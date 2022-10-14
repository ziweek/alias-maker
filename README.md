# alias-maker
<br>
<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
 </div>
 <br>
This simple application is made because I'm too lazy to type alias codes one by one. I thought it is not enough worth even to repeat typing same codes. In that sense, I really hope this application could also contribute to your laziness.

## How to use
### 1. Get ready to run code.

```
git clone https://github.com/ziweek/alias-maker.git
cd alias-maker
```

### 2. Run python script with two arguments.

One is the name of script, another is the upper dicrectory of targets.

```
python app.py /Users/basecamp/Dropbox/repo/project
```

### 3. Then, Copy the texts
```
--- alias maker ---
Detected Folders :
['ai-bot-service', 'bada-web-service', 'ziwook-web-service', 'slack-bot-service', 'kugods-website', 'bada-hsad']

# Copy below texts
# Paste the texts to ~/.zshrc
alias ai-bot-service="cd /Users/basecamp/Dropbox/repo/project/ai-bot-service; ls -l"
alias bada-web-service="cd /Users/basecamp/Dropbox/repo/project/bada-web-service; ls -l"
alias slack-bot-service="cd /Users/basecamp/Dropbox/repo/project/slack-bot-service; ls -l"
alias kugods-website="cd /Users/basecamp/Dropbox/repo/project/kugods-website; ls -l"
---             ---
```

### 4. Finally, Paste & Apply
```
open -e ~/.zshrc
```
```
source ~/.zshrc
```
