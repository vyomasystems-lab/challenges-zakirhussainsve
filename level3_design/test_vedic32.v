module test_vedic32;

reg [31:0]a;
reg [31:0]b;
wire [63:0]c;
integer i;
vedic_32x32 inst(a,b,c);

initial begin
$monitor($time, "a=%0d, b=%0d, c=%0d", a, b,c);
for(i=0;i<4;i=i+1) begin
a=$random;
b=$random;
#5;
end
#5;
$finish;
end
endmodule