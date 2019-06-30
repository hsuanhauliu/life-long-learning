# Go
"Go is an open source programming language that makes it easy to build simple, reliable, and efficient software." It is a statically typed, compiled programming language.

## Resources
### Guides
- [Documentation](https://golang.org/doc/)
- [Specifications](https://golang.org/ref/spec)
- [Packages](https://golang.org/pkg/): a list of Go's built-in packages.
- [Github](https://github.com/golang/go): Go's Github page.
- [Youtube](https://www.youtube.com/user/gocoding/featured): Go's Youtube channel.

### Tutorials
- [How to Write Go Code](https://golang.org/doc/code.html): a demonstration of Go program development.
- [A Tour of Go](https://tour.golang.org/welcome/1): an interactive online tutorial for basic Go programming.
- [Go by Example](https://gobyexample.com/): a collection of examples showing how Go works.
- [Writing, Building, Installing, and Testing Go Code](https://www.youtube.com/watch?v=XCsL89YtqCs&t=2s&list=LL_nJcU3CiKaa8b27n2dvsoQ&index=3): a video tutorial showing the development of a simple Go program.

### More
- [Go Playground](https://play.golang.org/): online sandbox for running Go programs.
- [Effective Go](https://golang.org/doc/effective_go.html): a documentation that shows effective ways of writing a Go program.

### Interesting read:
- [Defer, Panic, and Recover Key Words](https://blog.golang.org/defer-panic-and-recover)


## Getting Started
### Installation
If you're on an OS other than MacOS, follow the instruction [here](https://golang.org/doc/install).

On Mac, installation can be done via Homebrew.
```
brew install Go
```

To get the latest version of Go,
```
brew upgrade go
```

### Environment Setup
1. First, we need to create a workspace (directory that stores all of your Go source codes, packages, and binaries).  In Go, we typically keep all Go code in a single directory. This step is only required for your very first Go program on your machine. From the [documentation](https://golang.org/doc/code.html),

> A workspace is a directory hierarchy with two directories at its root:
1. src contains Go source files, and
2. bin contains executable commands.

We can also create a directory called *pkg* to store non-executable packages to be used for other Go code.

Go to the directory where you want to set up your workspace. Typically, we would create our workspace in the home directory.
```
cd ~/
mkdir go
cd go
```

Create the three directories where your source codes, packages, and binaries will reside.
```
mkdir bin pkg src
```

2. Set a GOPATH so that Go knows where to locate the workspace directory. You can add this to your shell resource file (i.e. .bash_profile or .zshrc) so that it will be loaded automatically in the future.
```
export GOPATH=$HOME/go
```

### Write Your Go Program
3. Each Go program should have its own repository(folder) in the go/src folder.

Create a folder to store codes that will be pushed to Github.
```
mkdir src/<program name>
cd src/<program name>
```

Every Go program needs a main package. At the very top of your code, the first line should be *package main* to mark the file as main.

After writing the code, we can either run the code directly or compile the code as executable.

```
# To run the program directly
go run <program main file>

# To compile the code into executable.
# Run this code in the root of the project repository
go build
./<program name>
```

We can install the executable binary to our workspace's bin directory
```
go install
```
The installed program will be in the $GOPATH/bin directory. For packages, they'll be in the $GOPATH/pkg directory.


>Tip: To make executing our program easier, we can add the bin directory to our system path. Again, this can be added to your shell resource file to make things easier to execute your future Go programs.
```
export $GOPATH/bin
<program name>
```


### Things To Keep in Mind

### Useful Go commands
go run <program-name>: runs the program directly.
