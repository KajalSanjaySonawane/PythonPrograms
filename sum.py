from pip._vendor.msgpack.fallback import xrange

print(sum(range(1,101)))   # normal time
#print(sum(xrange(1,101)))  #less heavy in the memory
