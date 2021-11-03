air_res = 0.83  #air resistce for cylindric objects
air_den = 1.225 #air density
surf_a  = W*D   #surface area affected by air resistance

def tot_air_res(v):
    return -1/2*(air_den*air_den*surf_a)*v**2

def gravity(h):
    return -G*m/(radius+h)**2

def net_force(v, h):
    return(tot_air_res(v) + gravity(h))

time = 5000
N = time/dt

x = np.zeros(N)         #posisjon
v = np.zeros(N)         #hastighet
a = np.zeros(N)         #akselerasjon
F = np.zeros(N)         #kraft

t = np.linspace(0,10,N) #tids array der dt = 0.01sekunder
for n in range (N-1):

    F[n] = net_force(v[n], h[n])
    a[n+1] = F/m
    v[n+1] = v[n] + a[n]*(t[n+1]-t[n])
    x[n+1] = x[n] + v[n]*(t[n+1]-t[n])

https://socratic.org/questions/an-electromagnet-can-exert-a-lifting-force-of-12-0n-when-it-operates-from-a-curr