# # Example 1

class myClass:
    variable = "some text"

    def myFunction(self):
        print("This is a message inside the class")

myobjectx = myClass() #creating an instance of the object
myobjectx.myFunction()


# #example 2

class MyClass():
    def method1(self):
        print("vviet")

    def method2(Self,someString):
        print("Project training:"+someString)


## excercise the class method

c = MyClass()
c.method1()
c.method2("Training is fun")


## example 3

class Movie:
    def movie_name(self,name):
        print("Movie name is :",name)

    def movie_rating(self,rating):
        print("Rating of the movie is :",rating)


## excercise the class method

c = Movie()
c.movie_name("KGF")
c.movie_rating(8)