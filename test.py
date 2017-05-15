def rec_tiler(origin, length, n, counter=0, thing=[]):
    hlen = length/2.
        
	    counter += 1
	        print "depth = %i & poly_len = %.2f // stop: %s" % (counter, hlen, n==counter)
		    
		        xy0 = origin
			    xy1 = origin[0], origin[1] + hlen
			        xy2 = origin[0] + hlen, origin[1]
				    xy3 = origin[0] + hlen, origin[1] + hlen
				        
					    for coord in [xy0, xy1, xy2, xy3]:
					            ans = rec_tiler(coord, hlen, n, counter, thing)
						        
							    print (xy0, xy1, xy2, xy3, hlen)
							        
								    if n == counter:
								            return None

ax = plubplot(111)
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 11)

tp = PolygonPatch(top_block, color='none', lw=6)
ax.add_patch(tp)

for sb in sub_block:
    subp = PolygonPatch(sb, alpha=0.3)
        ax.add_patch(subp)
	
	plt.show().subplot(111)

extent = (0, 0, 10, 10)
xy0 = (extent[0], extent[1])
xylen = extent[2] - extent[0]

def tiler(origin, length):
    hlen = length/2
        
	    xy0 = origin
	        xy1 = origin[0], origin[1] + hlen
		    xy2 = origin[0] + hlen, origin[1]
		        xy3 = origin[0] + hlen, origin[1] + hlen
			    
			        return (xy0, xy1, xy2, xy3, hlen)

				def build_polygon(origin, length):
				    x0, y0 = origin 
				        x1, y1 = np.array(origin) + length 
					    verts = [origin, (x0, y1), (x1, y1), (x1, y0)]
					        return Polygon(verts)
