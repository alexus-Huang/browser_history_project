from browser_history import BrowserHistory

history = BrowserHistory()

history.visit("google.com")
history.visit("youtube.com")
history.visit("leetcode.com")

print(history.back())       # youtube
print(history.back())       # google
print(history.forward())    # youtube

history.visit("github.com")

history.print_state()