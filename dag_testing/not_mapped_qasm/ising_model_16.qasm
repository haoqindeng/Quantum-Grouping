OPENQASM 2.0;
include "qelib1.inc";
qreg q[16];
creg c[16];
u1(4) q[0];
u1(4) q[1];
u1(4) q[2];
u1(4) q[3];
u1(4) q[4];
u1(4) q[5];
u1(4) q[6];
u1(4) q[7];
u1(4) q[8];
u1(4) q[9];
u1(4) q[10];
u1(4) q[11];
u1(4) q[12];
u1(4) q[13];
u1(4) q[14];
u1(4) q[15];
u1(0) q[0];
u1(0) q[1];
u1(0) q[2];
u1(0) q[3];
u1(0) q[4];
u1(0) q[5];
u1(0) q[6];
u1(0) q[7];
u1(0) q[8];
u1(0) q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(-1) q[15];
u1(-1) q[1];
u1(-1) q[3];
u1(0) q[5];
u1(0) q[7];
u1(0) q[9];
u1(-1) q[11];
u1(-1) q[13];
u1(-1) q[15];
cx q[0],q[1];
cx q[2],q[3];
cx q[4],q[5];
cx q[6],q[7];
cx q[8],q[9];
cx q[10],q[11];
cx q[12],q[13];
cx q[14],q[15];
u1(0) q[1];
u1(0) q[3];
u1(0) q[5];
u1(0) q[7];
u1(0) q[9];
u1(-1) q[11];
u1(-1) q[13];
u1(-1) q[15];
cx q[0],q[1];
cx q[2],q[3];
cx q[4],q[5];
cx q[6],q[7];
cx q[8],q[9];
cx q[10],q[11];
cx q[12],q[13];
cx q[14],q[15];
u1(0) q[1];
u1(0) q[2];
u1(0) q[3];
u1(0) q[4];
u1(0) q[5];
u1(0) q[6];
u1(0) q[7];
u1(0) q[8];
u1(-1) q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(4) q[0];
u1(4) q[15];
u1(1) q[2];
u1(-1) q[4];
u1(1) q[6];
u1(-1) q[8];
u1(-1) q[10];
u1(-1) q[12];
u1(-1) q[14];
u1(-1) q[0];
u1(-1) q[15];
cx q[1],q[2];
cx q[3],q[4];
cx q[5],q[6];
cx q[7],q[8];
cx q[9],q[10];
cx q[11],q[12];
cx q[13],q[14];
u1(4) q[0];
u1(4) q[15];
u1(0) q[2];
u1(0) q[4];
u1(0) q[6];
u1(0) q[8];
u1(-1) q[10];
u1(-1) q[12];
u1(-1) q[14];
u1(0) q[0];
u1(-1) q[15];
cx q[1],q[2];
cx q[3],q[4];
cx q[5],q[6];
cx q[7],q[8];
cx q[9],q[10];
cx q[11],q[12];
cx q[13],q[14];
u1(0) q[0];
u1(-1) q[15];
u1(4) q[1];
u1(4) q[2];
u1(4) q[3];
u1(4) q[4];
u1(4) q[5];
u1(4) q[6];
u1(4) q[7];
u1(4) q[8];
u1(4) q[9];
u1(4) q[10];
u1(4) q[11];
u1(4) q[12];
u1(4) q[13];
u1(4) q[14];
u1(-1) q[15];
u1(-1) q[1];
u1(-1) q[2];
u1(-1) q[3];
u1(-1) q[4];
u1(-1) q[5];
u1(-1) q[6];
u1(-1) q[7];
u1(-1) q[8];
u1(-1) q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(4) q[1];
u1(4) q[2];
u1(4) q[3];
u1(4) q[4];
u1(4) q[5];
u1(4) q[6];
u1(4) q[7];
u1(4) q[8];
u1(4) q[9];
u1(4) q[10];
u1(4) q[11];
u1(4) q[12];
u1(4) q[13];
u1(4) q[14];
u1(0) q[1];
u1(1) q[2];
u1(-1) q[3];
u1(-1) q[4];
u1(0) q[5];
u1(1) q[6];
u1(0) q[7];
u1(1) q[8];
u1(-1) q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(0) q[1];
u1(-1) q[2];
u1(1) q[3];
u1(0) q[4];
u1(0) q[5];
u1(0) q[6];
u1(0) q[7];
u1(0) q[8];
u1(0) q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(-3) q[1];
u1(-4) q[3];
u1(-1) q[5];
u1(2) q[7];
u1(0) q[9];
u1(-1) q[11];
u1(-1) q[13];
cx q[14],q[15];
cx q[0],q[1];
cx q[2],q[3];
cx q[4],q[5];
cx q[6],q[7];
cx q[8],q[9];
cx q[10],q[11];
cx q[12],q[13];
u1(-1) q[15];
u1(1) q[1];
u1(2) q[3];
u1(0) q[5];
u1(-1) q[7];
u1(0) q[9];
u1(-1) q[11];
u1(-1) q[13];
cx q[14],q[15];
cx q[0],q[1];
cx q[2],q[3];
cx q[4],q[5];
cx q[6],q[7];
cx q[8],q[9];
cx q[10],q[11];
cx q[12],q[13];
u1(-1) q[14];
u1(4) q[15];
u1(0) q[1];
u1(0) q[2];
u1(0) q[3];
u1(0) q[4];
u1(1) q[5];
u1(-1) q[6];
u1(0) q[7];
u1(0) q[8];
u1(-1) q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(4) q[0];
u1(0) q[15];
u1(3) q[2];
u1(-3) q[4];
u1(4) q[6];
u1(-3) q[8];
u1(-1) q[10];
u1(-1) q[12];
cx q[13],q[14];
u1(0) q[0];
u1(4) q[15];
cx q[1],q[2];
cx q[3],q[4];
cx q[5],q[6];
cx q[7],q[8];
cx q[9],q[10];
cx q[11],q[12];
u1(-1) q[14];
u1(4) q[0];
u1(-1) q[15];
u1(-1) q[2];
u1(1) q[4];
u1(-2) q[6];
u1(1) q[8];
u1(-1) q[10];
u1(-1) q[12];
cx q[13],q[14];
u1(0) q[0];
u1(-1) q[15];
cx q[1],q[2];
cx q[3],q[4];
cx q[5],q[6];
cx q[7],q[8];
cx q[9],q[10];
cx q[11],q[12];
u1(4) q[13];
u1(4) q[14];
u1(-1) q[0];
u1(-1) q[15];
u1(4) q[1];
u1(4) q[2];
u1(4) q[3];
u1(4) q[4];
u1(4) q[5];
u1(4) q[6];
u1(4) q[7];
u1(4) q[8];
u1(4) q[9];
u1(4) q[10];
u1(4) q[11];
u1(4) q[12];
u1(0) q[13];
u1(0) q[14];
u1(0) q[1];
u1(0) q[2];
u1(0) q[3];
u1(0) q[4];
u1(0) q[5];
u1(0) q[6];
u1(0) q[7];
u1(0) q[8];
u1(0) q[9];
u1(0) q[10];
u1(0) q[11];
u1(0) q[12];
u1(4) q[13];
u1(4) q[14];
u1(4) q[1];
u1(4) q[2];
u1(4) q[3];
u1(4) q[4];
u1(4) q[5];
u1(4) q[6];
u1(4) q[7];
u1(4) q[8];
u1(4) q[9];
u1(4) q[10];
u1(4) q[11];
u1(4) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(0) q[1];
u1(0) q[2];
u1(0) q[3];
u1(0) q[4];
u1(0) q[5];
u1(0) q[6];
u1(0) q[7];
u1(0) q[8];
u1(0) q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(1) q[1];
u1(-1) q[2];
u1(1) q[3];
u1(0) q[4];
u1(0) q[5];
u1(1) q[6];
u1(-1) q[7];
u1(0) q[8];
u1(0) q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(-1) q[13];
cx q[14],q[15];
u1(-6) q[1];
u1(-7) q[3];
u1(-2) q[5];
u1(4) q[7];
u1(1) q[9];
u1(-1) q[11];
cx q[12],q[13];
u1(-1) q[15];
cx q[0],q[1];
cx q[2],q[3];
cx q[4],q[5];
cx q[6],q[7];
cx q[8],q[9];
cx q[10],q[11];
u1(-1) q[13];
cx q[14],q[15];
u1(3) q[1];
u1(3) q[3];
u1(1) q[5];
u1(-2) q[7];
u1(0) q[9];
u1(-1) q[11];
cx q[12],q[13];
u1(-1) q[14];
u1(4) q[15];
cx q[0],q[1];
cx q[2],q[3];
cx q[4],q[5];
cx q[6],q[7];
cx q[8],q[9];
cx q[10],q[11];
u1(-1) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(0) q[15];
u1(1) q[1];
u1(-1) q[2];
u1(-1) q[3];
u1(1) q[4];
u1(1) q[5];
u1(-1) q[6];
u1(-1) q[7];
u1(1) q[8];
u1(-1) q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
cx q[13],q[14];
u1(4) q[0];
u1(4) q[15];
u1(5) q[2];
u1(-5) q[4];
u1(7) q[6];
u1(-5) q[8];
u1(-1) q[10];
cx q[11],q[12];
u1(-1) q[14];
u1(0) q[0];
u1(-1) q[15];
cx q[1],q[2];
cx q[3],q[4];
cx q[5],q[6];
cx q[7],q[8];
cx q[9],q[10];
u1(-1) q[12];
cx q[13],q[14];
u1(4) q[0];
u1(-1) q[15];
u1(-2) q[2];
u1(2) q[4];
u1(-3) q[6];
u1(2) q[8];
u1(-1) q[10];
cx q[11],q[12];
u1(4) q[13];
u1(4) q[14];
u1(0) q[0];
u1(-1) q[15];
cx q[1],q[2];
cx q[3],q[4];
cx q[5],q[6];
cx q[7],q[8];
cx q[9],q[10];
u1(4) q[11];
u1(4) q[12];
u1(0) q[13];
u1(0) q[14];
u1(-2) q[0];
u1(4) q[1];
u1(4) q[2];
u1(4) q[3];
u1(4) q[4];
u1(4) q[5];
u1(4) q[6];
u1(4) q[7];
u1(4) q[8];
u1(4) q[9];
u1(4) q[10];
u1(0) q[11];
u1(0) q[12];
u1(4) q[13];
u1(4) q[14];
u1(0) q[1];
u1(0) q[2];
u1(0) q[3];
u1(0) q[4];
u1(0) q[5];
u1(0) q[6];
u1(0) q[7];
u1(0) q[8];
u1(0) q[9];
u1(0) q[10];
u1(4) q[11];
u1(4) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(4) q[1];
u1(4) q[2];
u1(4) q[3];
u1(4) q[4];
u1(4) q[5];
u1(4) q[6];
u1(4) q[7];
u1(4) q[8];
u1(4) q[9];
u1(4) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(0) q[1];
u1(0) q[2];
u1(0) q[3];
u1(0) q[4];
u1(0) q[5];
u1(0) q[6];
u1(0) q[7];
u1(0) q[8];
u1(0) q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(-1) q[13];
cx q[14],q[15];
u1(2) q[1];
u1(-2) q[2];
u1(2) q[3];
u1(0) q[4];
u1(0) q[5];
u1(1) q[6];
u1(-1) q[7];
u1(0) q[8];
u1(0) q[9];
u1(-1) q[10];
u1(-1) q[11];
cx q[12],q[13];
u1(-1) q[15];
u1(-8) q[1];
u1(-10) q[3];
u1(-3) q[5];
u1(6) q[7];
u1(2) q[9];
cx q[10],q[11];
u1(-1) q[13];
cx q[14],q[15];
cx q[0],q[1];
cx q[2],q[3];
cx q[4],q[5];
cx q[6],q[7];
cx q[8],q[9];
u1(-1) q[11];
cx q[12],q[13];
u1(-1) q[14];
u1(4) q[15];
u1(4) q[1];
u1(5) q[3];
u1(1) q[5];
u1(-3) q[7];
u1(-1) q[9];
cx q[10],q[11];
u1(-1) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(0) q[15];
cx q[0],q[1];
cx q[2],q[3];
cx q[4],q[5];
cx q[6],q[7];
cx q[8],q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
cx q[13],q[14];
u1(4) q[15];
u1(1) q[1];
u1(-1) q[2];
u1(-1) q[3];
u1(1) q[4];
u1(2) q[5];
u1(-2) q[6];
u1(-1) q[7];
u1(1) q[8];
u1(-1) q[9];
u1(-1) q[10];
cx q[11],q[12];
u1(-1) q[14];
u1(4) q[0];
u1(-1) q[15];
u1(7) q[2];
u1(-7) q[4];
u1(10) q[6];
u1(-7) q[8];
cx q[9],q[10];
u1(-1) q[12];
cx q[13],q[14];
u1(0) q[0];
u1(-1) q[15];
cx q[1],q[2];
cx q[3],q[4];
cx q[5],q[6];
cx q[7],q[8];
u1(-1) q[10];
cx q[11],q[12];
u1(4) q[0];
u1(4) q[13];
u1(4) q[14];
u1(-1) q[15];
u1(-3) q[2];
u1(3) q[4];
u1(-5) q[6];
u1(3) q[8];
cx q[9],q[10];
u1(4) q[11];
u1(4) q[12];
u1(0) q[13];
u1(0) q[14];
u1(0) q[0];
cx q[1],q[2];
cx q[3],q[4];
cx q[5],q[6];
cx q[7],q[8];
u1(4) q[9];
u1(4) q[10];
u1(0) q[11];
u1(0) q[12];
u1(4) q[13];
u1(4) q[14];
u1(-2) q[0];
u1(4) q[1];
u1(4) q[2];
u1(4) q[3];
u1(4) q[4];
u1(4) q[5];
u1(4) q[6];
u1(4) q[7];
u1(4) q[8];
u1(0) q[9];
u1(0) q[10];
u1(4) q[11];
u1(4) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(0) q[1];
u1(0) q[2];
u1(0) q[3];
u1(0) q[4];
u1(0) q[5];
u1(0) q[6];
u1(0) q[7];
u1(0) q[8];
u1(4) q[9];
u1(4) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(4) q[1];
u1(4) q[2];
u1(4) q[3];
u1(4) q[4];
u1(4) q[5];
u1(4) q[6];
u1(4) q[7];
u1(4) q[8];
u1(0) q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(-1) q[13];
cx q[14],q[15];
u1(0) q[1];
u1(0) q[2];
u1(0) q[3];
u1(0) q[4];
u1(0) q[5];
u1(0) q[6];
u1(0) q[7];
u1(0) q[8];
u1(0) q[9];
u1(-1) q[10];
u1(-1) q[11];
cx q[12],q[13];
u1(-1) q[15];
u1(2) q[1];
u1(-3) q[2];
u1(3) q[3];
u1(-1) q[4];
u1(1) q[5];
u1(1) q[6];
u1(-1) q[7];
u1(0) q[8];
u1(2) q[9];
cx q[10],q[11];
u1(-1) q[13];
cx q[14],q[15];
u1(-10) q[1];
u1(-12) q[3];
u1(-4) q[5];
u1(7) q[7];
cx q[8],q[9];
u1(-1) q[11];
cx q[12],q[13];
u1(-1) q[14];
u1(4) q[15];
cx q[0],q[1];
cx q[2],q[3];
cx q[4],q[5];
cx q[6],q[7];
u1(-1) q[9];
cx q[10],q[11];
u1(-1) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(1) q[15];
u1(5) q[1];
u1(6) q[3];
u1(2) q[5];
u1(-3) q[7];
cx q[8],q[9];
u1(-1) q[10];
u1(-1) q[11];
u1(-1) q[12];
cx q[13],q[14];
u1(4) q[15];
cx q[0],q[1];
cx q[2],q[3];
cx q[4],q[5];
cx q[6],q[7];
u1(2) q[8];
u1(-1) q[9];
u1(-1) q[10];
cx q[11],q[12];
u1(-1) q[14];
u1(-1) q[15];
u1(2) q[1];
u1(-2) q[2];
u1(-2) q[3];
u1(2) q[4];
u1(3) q[5];
u1(-3) q[6];
u1(-2) q[7];
u1(-9) q[8];
cx q[9],q[10];
u1(-1) q[12];
cx q[13],q[14];
u1(4) q[0];
u1(9) q[2];
u1(-9) q[4];
u1(13) q[6];
cx q[7],q[8];
u1(-1) q[10];
cx q[11],q[12];
u1(1) q[0];
u1(4) q[13];
u1(4) q[14];
cx q[1],q[2];
cx q[3],q[4];
cx q[5],q[6];
u1(4) q[8];
cx q[9],q[10];
u1(4) q[0];
u1(4) q[11];
u1(4) q[12];
u1(1) q[13];
u1(1) q[14];
u1(-4) q[2];
u1(4) q[4];
u1(-6) q[6];
cx q[7],q[8];
u1(4) q[9];
u1(4) q[10];
u1(1) q[11];
u1(1) q[12];
u1(4) q[13];
u1(4) q[14];
u1(0) q[0];
cx q[1],q[2];
cx q[3],q[4];
cx q[5],q[6];
u1(4) q[7];
u1(4) q[8];
u1(1) q[9];
u1(1) q[10];
u1(4) q[11];
u1(4) q[12];
u1(-1) q[13];
u1(-1) q[14];
u1(4) q[1];
u1(4) q[2];
u1(4) q[3];
u1(4) q[4];
u1(4) q[5];
u1(4) q[6];
u1(1) q[7];
u1(1) q[8];
u1(4) q[9];
u1(4) q[10];
u1(-1) q[11];
u1(-1) q[12];
u1(1) q[1];
u1(1) q[2];
u1(1) q[3];
u1(1) q[4];
u1(1) q[5];
u1(1) q[6];
u1(4) q[7];
u1(4) q[8];
u1(1) q[9];
u1(-1) q[10];
u1(4) q[1];
u1(4) q[2];
u1(4) q[3];
u1(4) q[4];
u1(4) q[5];
u1(4) q[6];
u1(0) q[7];
u1(-1) q[8];
u1(0) q[1];
u1(-1) q[2];
u1(1) q[3];
u1(1) q[4];
u1(0) q[5];
u1(-1) q[6];
