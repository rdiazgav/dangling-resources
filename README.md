# aws dangling resources


## Getting started

The scope of this project is to scout the ways to find out dangling resources within the AWS account and print all these resources for housekeeping purposes

## Add your resources

from dangling_resources.py I call (import) to others .py, the idea is making it modular and add more resources to find out

resources included so far:

    - Unattached EBS volumes
    - ELB without attached instances 
    - ....
    - 

## Example report


    $ python dangling_resources.py 

    List of all ELBs without instances attached
    ===========================================
    ELB aa103bef385f041faa442b2007c2bf43 has no instances attached.
    ELB a7199c131cc974f76b0c2d7fff6b1d22 has no instances attached.
    ELB aa103bef385f041faa442b2007c2bf43 has no instances attached.
    [...]

    list of unattached EBS Volumes
    ==============================
    Volume ID: vol-08f3f85b3070a54cf Size: 500 Availability Zone: eu-west-3b 
    Volume ID: vol-01a620115392f1563 Size: 10 Availability Zone: eu-west-3b 
    Volume ID: vol-0574983818f97ef61 Size: 500 Availability Zone: eu-west-3b 
    [...]

    Security group without instances attached
    =========================================
    sg-0a4c53cd55fed8f5e has not instances associated.
    sg-0c9e262024da39da3 has not instances associated.  
    sg-06f3124d26da65612 has not instances associated.
    [...]

    list of unused/unttached EIPs
    =============================
    Region: eu-west-1, IP Address: 52.49.241.10
    Region: eu-west-1, IP Address: 54.229.35.35
    Region: ca-central-1, IP Address: 15.223.137.247
    [...]

    List of unused network interfaces
    =================================
    Region: ca-central-1, Network Interface Id: eni-00ddc205c6c02bd9f
    Region: ca-central-1, Network Interface Id: eni-09a4edd6936d233ef
    Region: us-east-1, Network Interface Id: eni-0aed714fbcd49095d
    [...]
