);

  assign clk_i = (rst_n == 1) ? clk : 0;
  assign activeDataCycle = hReady && (hTrans != 0);

  covergroup myAhbCg @(negedge clk_i);
