module myAxiStreamingCgModule
#(
  parameter TDATA_WIDTH = 8,
            TSTRB_WIDTH = TDATA_WIDTH/8,
            TKEEP_WIDTH = 4,
            TID_WIDTH   = 4,
            TDEST_WIDTH = 4,
            TUSER_WIDTH = 4
)
(
  input                   clk,
  input                   rst_n,

  input                   tValid,
  input                   tReady,
  input [TDATA_WIDTH-1:0] tData,
  input [TSTRB_WIDTH-1:0] tStrb,
  input [TKEEP_WIDTH-1:0] tKeep,
  input                   tLast,
  input [TID_WIDTH-1:0]   tId,
  input [TDEST_WIDTH-1:0] tDest,
  input [TUSER_WIDTH-1:0] tUser
);

  assign clk_i = (rst_n == 1) ? clk : 0;
  assign activeDataCycle = tValid && tReady;

  covergroup myAxiStreamingCg @(posedge clk_i);
    activeDataCycle : coverpoint activeDataCycle
    {
      bins active = { 1 };
    }
    tDataToggle : coverpoint tData
    {
      bins bit0_is_1 = { 8'bxxxxxxx1 } iff (activeDataCycle);
      bins bit0_is_0 = { 8'bxxxxxxx0 } iff (activeDataCycle);
      bins bit1_is_1 = { 8'bxxxxxx1x } iff (activeDataCycle);
      bins bit1_is_0 = { 8'bxxxxxx0x } iff (activeDataCycle);
      bins bit2_is_1 = { 8'bxxxxx1xx } iff (activeDataCycle);
      bins bit2_is_0 = { 8'bxxxxx0xx } iff (activeDataCycle);
      bins bit3_is_1 = { 8'bxxxx1xxx } iff (activeDataCycle);
      bins bit3_is_0 = { 8'bxxxx0xxx } iff (activeDataCycle);
      bins bit4_is_1 = { 8'bxxx1xxxx } iff (activeDataCycle);
      bins bit4_is_0 = { 8'bxxx0xxxx } iff (activeDataCycle);
      bins bit5_is_1 = { 8'bxx1xxxxx } iff (activeDataCycle);
      bins bit5_is_0 = { 8'bxx0xxxxx } iff (activeDataCycle);
      bins bit6_is_1 = { 8'bx1xxxxxx } iff (activeDataCycle);
      bins bit6_is_0 = { 8'bx0xxxxxx } iff (activeDataCycle);
      bins bit7_is_1 = { 8'b1xxxxxxx } iff (activeDataCycle);
      bins bit7_is_0 = { 8'b0xxxxxxx } iff (activeDataCycle);
    }
    tStrbValues : coverpoint tStrb iff (activeDataCycle);
    tKeepValues : coverpoint tKeep iff (activeDataCycle);
    tLastToggle : coverpoint tLast
    {
      bins bit0_is_1 = { 1'b1 } iff (activeDataCycle);
      bins bit0_is_0 = { 1'b0 } iff (activeDataCycle);
    }
    tIdValues : coverpoint tId iff (activeDataCycle);
    tDestValues : coverpoint tDest iff (activeDataCycle);
    tUserValues : coverpoint tUser iff (activeDataCycle);
  endgroup

endmodule

