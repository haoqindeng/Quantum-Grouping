OPENQASM 2.0;
include "qelib1.inc";
qreg q[16];
creg c[16];
u1(4) q[0];
u1(7) q[2];
u1(7) q[1];
u1(7) q[0];
cx q[0],q[1];
swap q[1],q[2];
cx q[1],q[0];
cx q[2],q[1];
u1(8) q[0];
swap q[0],q[1];
cx q[2],q[1];
u1(7) q[0];
u1(8) q[2];
u1(8) q[1];
cx q[0],q[1];
swap q[1],q[2];
cx q[1],q[0];
cx q[2],q[1];
u1(4) q[0];
cx q[2],q[1];
cx q[1],q[2];
swap q[1],q[2];
cx q[0],q[1];
cx q[1],q[2];
