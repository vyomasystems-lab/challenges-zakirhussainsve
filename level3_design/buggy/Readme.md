# This is an example for buggy design of vedic multiplier

![image](https://user-images.githubusercontent.com/109347684/182183594-5a7dcd78-ba99-46a2-b879-b87fec5647a8.png)


1. Verification environment:

RTL design is developed using Verilog HDL for vedic-32 multiplier; And the functional verification is using python framework.


2. Test scenario:

![image](https://user-images.githubusercontent.com/109347684/182184808-968d4690-593e-414c-a730-13d36f7b06bd.png)


Test case assumes that designer had done mistake in using multiplication operator, it assumes that, the designer instead using the multiplication operator desiner uses
addition operator.


3. Design bug:

![image](https://user-images.githubusercontent.com/109347684/182186497-7d3f26ba-dfde-4fdd-b442-7b23b306b955.png)
