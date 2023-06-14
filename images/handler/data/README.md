
```
      __  ___________  __    __       __       ______   __   ___  
     /""\("     _   ")/" |  | "\     /""\     /" _  "\ |/"| /  ") 
    /    \)__/  \\__/(:  (__)  :)   /    \   (: ( \___)(: |/   /  
   /' /\  \  \\_ /    \/      \/   /' /\  \   \/ \     |    __/   
  //  __'  \ |.  |    //  __  \\  //  __'  \  //  \ _  (// _  \   
 /   /  \\  \\:  |   (:  (  )  :)/   /  \\  \(:   _) \ |: | \  \  
(___/    \___)\__|    \__|  |__/(___/    \___)\_______)(__|  \__) 
                                                                  
                                          ____  ____  _ ____       _       
                                     /\ /\___ \|___ \/ | ___|  ___(_)_ __  
                                    / / \ \__) | __) | |___ \ |_  / | '_ \ 
                                    \ \_/ / __/ / __/| |___) | / /| | |_) |
                                     \___/_____|_____|_|____(_)___|_| .__/ 
                                                                    |_|                                                               
```

# You were trapped ! 

Hey you ! 
You wanted to access "https://__ATHACK_DOMAIN__/__ATHACK_PATH__" right ? 
Well, you didn't see the little characters and dumbly copy/pasted the command into your terminal ... 

BAD IDEA ! 

The command you pasted contained the unicode character "u2215" that is confusing with the regular "/" character ! 
What does that mean ? that means that instead of accessing the domain "__ATHACK_DOMAIN__", you accessed "u2215.zip" and were delivered something else you expected ... 

# How to be better ? 

First, analyze what command you are copy pasting and avoid piping a download to a bash script.  
Second, when you download things, compare the hash of the downloaded files against the expected to be sure you downloaded the correct files. 
