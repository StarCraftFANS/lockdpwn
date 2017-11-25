%{
    matlab ==> �������ڵ���, �������� ������Ʈ���� string stability�� �˻��ϴ� �ڵ�
%}

% set parameters
k1 = 0.0244;
k2 = -1.7211;
q = 0.2;
tau = 1.24;

% find out string stability
s = tf('s');
H1 = (-k2 *s + k1) / (q*s^3 + (1+k2*tau)*s^2 - k2*s + k1);
H2 = (tau*q*s^2 + (k2*tau+1)*tau*s) / (q*s^3 + (1+k2*tau)*s^2 - k2*s + k1);

bode(H1); grid  % should be less than 1