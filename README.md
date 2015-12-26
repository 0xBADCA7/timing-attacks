# ⚠  Warning: This is a work in progress / incomplete work.

# Practical timing attacks
In this repository one can find a vulnerable to timing attacks web application and Mathematica code to exploit it.

## Requirements
* Python 3
* Flask for Python
* Mathematica 10+

## Run
Change directory to `web app` and then run `python3 ./main.py`. 

# Timing attacks
Timing attack is a common way to exploit the fact that computation can be measured and conclusions be made based on the measurements. Timing attacks, perhaps, can be applied to anything that can be measured (from the computing perspective). We're interested in how long an operation takes to be completed compared to another.

We query a remote or local system with at least two queries. By differentiating two or more inquiries we can compare the computation time length. If an operation takes longer than another one then most likely there's more processing required by that operation compared to another one due to CPU cycles, I/O, etc. 

Knowing that one operation takes longer than another one can hint at the program flow within the examined system. If we take a web application as an example of such system, with known source code (FLOSS or code is accessible through various means e.g. data leak), then we may have a chance to differentiate between two code branches that run in different time. 

As a side note, timing attacks can be found in both – hardware and software. Timing attacks on cryptographic devices are similar. For example, in one of the attacks [1,2] we would measure the difference in time it takes for a piece of silicon to (read, CPU cycles) compute a private key exponent using the square-and-multiply *modular exponentiation* algorithm (typical for embedded systems) which contains binary 1 and the one that contains 0 in that position. In this modular exponentiation algorithm the code branch that took longer time corresponded to binary 1 in the exponent. It was possible to recover all the bits of the private exponent by timing the differences in computation. Today things are a little *bit* better.

Timing attacks can even happen to wetware: we sometimes can infer that people know something based on how quickly they respond. The *idea* is the same in that it takes more brain processing to react to events we already know of, although it's on the boundary of science and prejudice.

### Vulnerable web application

Getting back to vulnerabilities over the Internet, let's consider a vulnerable web application which authenticates users based on the password they provide. The sources of such sample application are located in the `webapp` folder. This deliberately vulnerable application would compare the user–provided password string to a predefined one which is a secret. We will try to infer what the secret is by observing the application response time. Note that it does not have to be a secret "password" – it can be a hash or even an empty request. It can even be code that would return if a user is not found in the database which means we can figure out the correct system's users. Our main aim is to figure out which input is plausible.

There are multiple ways to introduce such vulnerabilities in the code. In the `webapp/index.py` we have several of them to play around with. One of them is nearly impractical but can help demonstrate the tools used to measure requests. Others are way better and commonly found in badly written web apps.

### Measuring latency

There's a lot that can influence latency – other applications that require network, CPU time (e.g. a side process clocking to 100%), noise from a powerful video card et al. At times, the resolution we need is nanoseconds, however not all network devices (network cards) support that and only "see" microseconds; or a library to be used to parse captured network streams may not be nanosecond–friendly. Here, we are looking at a very primitive and effective way to analyze latencies that do not require that.

### References

1. Kocher, Paul C. "Timing attacks on implementations of Diffie–Hellman, RSA, DSS, and other systems." Advances in Cryptology—CRYPTO’96. Springer Berlin Heidelberg, 1996.

2. Schindler, Werner. "A timing attack against RSA with the chinese remainder theorem." Cryptographic Hardware and Embedded Systems—CHES 2000. Springer Berlin Heidelberg, 2000. APA	
  
