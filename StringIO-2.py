import StringIO
import string,sys
stdout = sys.stdout
sys.stdout = file = StringIO.StringIO()
print "a"
sys.stdout = stdout
print string.upper(file.getvalue())
