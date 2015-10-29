);

  assign clk_i = (rst_n == 1) ? clk : 0;
  assign activeDataCycle = tValid && tReady;

  covergroup myAxiStreamingCg @(negedge clk_i);
