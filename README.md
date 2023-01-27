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
    ELB aa103bef385f041fsd442b2007c2bf43 has no instances attached.
    ELB a7199c131cc974f76sdc2d7fff6b1d22 has no instances attached.
    ELB aa103bef385f041gaa4sfsd0gfcgbf43 has no instances attached.
    [...]

    list of unattached EBS Volumes
    ==============================
    Volume ID: vol-08f3f85b3230a54cf Size: 500 Availability Zone: eu-west-3b 
    Volume ID: vol-01a620123392f1563 Size: 10 Availability Zone: eu-west-3b 
    Volume ID: vol-0574983811297ef61 Size: 500 Availability Zone: eu-west-3b 
    [...]

    Security group without instances attached
    =========================================
    sg-0a4c53cd551238f5e has not instances associated.
    sg-0c9e262024da334a3 has not instances associated.  
    sg-06f3124d264324612 has not instances associated.
    [...]

    list of unused/unttached EIPs
    =============================
    Region: eu-west-1, IP Address: 152.49.241.10
    Region: eu-west-1, IP Address: 154.229.35.35
    Region: ca-central-1, IP Address: 115.223.137.247
    [...]

    List of unused network interfaces
    =================================
    Region: ca-central-1, Network Interface Id: eni-00ddc205c6c44bd9f
    Region: ca-central-1, Network Interface Id: eni-09a4edd6936d233ef
    Region: us-east-1, Network Interface Id: eni-0aed714fbcd49092s
    [...]
