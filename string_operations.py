n1 = 15
n2 = 25
print "maximum of "+ n1 +"and " + n2 +"is " +max(n1,n2)
#maximum of 15 and 25 is 25

print "maximum of {0} and {1} is {2}".format(n1,n2,max(n1,n2))
#maximum of 15 and 25 is 25

print "maximum of %i and %i is %d" % (n1,n2,max(n1,n2))
#maximum of 15 and 25 is 25
""" where %i and %d are placeholders for integer and digit respectively """

""" from line 6 those {0},{1} ad {2} are called tuple indexes which should match count of the arguments to `format()`.
order of those indexed can be changed"""

print "maximum of {1} and {0} is {2}".format(n1,n2,max(n1,n2))
#maximum of 25 and 15 is 25
