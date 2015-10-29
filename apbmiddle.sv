);

  assign clk_i = (rst_n == 1) ? clk : 0;
  assign activeDataCycle = pEnable && pReady;

  covergroup myApbCg @(negedge clk_i);
