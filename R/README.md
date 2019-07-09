# R
R is a command line driven program developed for performing statistics analysis.

## Resources
- [Quick-R by DataCamp](https://www.statmethods.net/r-tutorial/index.html)

## Things to Know
- Workspace: the workspace is your current R working environment and includes any user-defined objects. At the end of an R session, the user can save an image of the current workspace that is automatically reloaded the next time R is started.

## Assignment Operator
In R, *<-* is more commonly used to assign values to variables. Read more about the difference between <- and = [here](https://stackoverflow.com/questions/6140694/is-there-a-technical-difference-between-and).


sapply(data, function)
Apply statistic functions (i.e. mean, sd, var, etc.) to the data.
```
sapply(data, mean, na.rm=TRUE)
```

Packages
```
.libPaths() # get library location
library()   # see all packages installed
search()    # see packages currently loaded
install.packages("package_name")  # install new package
```

Help
```
help.start()    # general help
help(foo)       # help about function foo
?foo            # same thing
apropos("foo")  # list all functions containing string foo
example(foo)    # show an example of function foo
```

Input/Output
```
source("file_path") # input a file
# append option: controls whether output overwrites or adds to a file
# split option: determines if output is also sent to the screen as well as the output file
sink("output", append=FALSE, split="FALSE") # redirect output to a file
sink()  # return output to the terminal console
```
