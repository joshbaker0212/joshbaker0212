The CCValidator python file was my first attempt at the credit card validation tool challenge located here: https://www.hackerrank.com/challenges/validating-credit-card-number/problem

The first iteration worked but I could not enter the number of credit cards to be validated so I built a second iteration which is the CCValidator2.py


The static web application I built using AWS console and utilizing an EC2 server and a load balancer to allow for scaling and taking advantage of the load balancers ability to force port 80 requests to https/443

the static web application is located at https://webserverlb-1229222875.us-east-1.elb.amazonaws.com

The terraform file included named main.tf is what I used to build the EC2 server and its web app/static page.

My web monitoring tool which I also built in python and is the file webmonitor.py It basically just reads the website and then converts the input into a hash, then rereads the website and stores that in a new hash and then compares both hashes. If they match it just continuues to repeat. If they do not match it outputs an alert via the print statement.
