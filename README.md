# reinforcementLearning_practicalWoks

## lecture notes 

### dynamic programming vs monte carlo simulations vs temperal difference 
![image](https://user-images.githubusercontent.com/91216581/206213936-43cf218f-e40f-4d46-8dff-90b8db5a0285.png)
![image](https://user-images.githubusercontent.com/91216581/206213954-02652d2d-4ec5-4832-afcb-32e268d3e30b.png)
![image](https://user-images.githubusercontent.com/91216581/206213963-91a8a3e6-0f1d-445e-bbd1-f9c30a5cfb16.png)


### sarsa vs q-learning

sarsa use the same policy for behaviral policy and target policy,while q-learning use different policies. it pursues the max aka. greedy policy for the learning fo the target policy.

![Screenshot 2022-12-07 at 15 57 14](https://user-images.githubusercontent.com/91216581/206212700-45861640-66e6-4bd3-837d-9d3f7dc4a107.png)
#### math summary
![Screenshot 2022-12-07 at 16 59 17](https://user-images.githubusercontent.com/91216581/206228142-c93da78c-b605-4f6a-88eb-d029c4bae18f.png)

#### q-learning example
reference : https://www.youtube.com/watch?v=l06oSHOR0x4
![Screenshot 2022-12-07 at 16 24 23](https://user-images.githubusercontent.com/91216581/206219548-edf582c6-a981-4375-a263-4dff8bfe9070.png)
![Screenshot 2022-12-07 at 16 26 05](https://user-images.githubusercontent.com/91216581/206219962-e24d364f-e662-4d55-b647-b95349883f41.png)
![Screenshot 2022-12-07 at 16 24 36](https://user-images.githubusercontent.com/91216581/206219600-2e235a4a-597d-4d4a-842f-629dcde7533f.png)
![Screenshot 2022-12-07 at 16 23 29](https://user-images.githubusercontent.com/91216581/206219374-4754ffad-31d1-4adf-b843-a154f297f3f4.png)

#### divergence problem of q-learning.
#### on policy vs off policy
