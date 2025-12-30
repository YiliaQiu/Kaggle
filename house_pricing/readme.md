|varibles|explain|values / q0-q4 / abnormal|construct|
|---|---|---|---|
|SalePrice| 房产销售价格，以美元计价。所要预测的目标变量|\|log|
|MSSubClass| 住所类型|20:	1-STORY 1946 & NEWER ALL STYLES<br>30:	1-STORY 1945 & OLDER<br>40:	1-STORY W/FINISHED ATTIC ALL AGES<br>45:	1-1/2 STORY - UNFINISHED ALL AGES<br>50:	1-1/2 STORY FINISHED ALL AGES<br>60:	2-STORY 1946 & NEWER<br>70:	2-STORY 1945 & OLDER<br>75:	2-1/2 STORY ALL AGES<br>80:	SPLIT OR MULTI-LEVEL<br>85:	SPLIT FOYER<br>90:	DUPLEX - ALL STYLES AND AGES<br>120:	1-STORY PUD (Planned Unit Development) - 1946 & NEWER<br>150:	1-1/2 STORY PUD - ALL AGES<br>160:	2-STORY PUD - 1946 & NEWER<br>180:	PUD - MULTILEVEL - INCL SPLIT LEV/FOYER<br>190:	2 FAMILY CONVERSION - ALL STYLES AND AGES|类别变量|
|MSZoning| The general zoning classification 区域分类|A:	Agriculture<br>C:	Commercial<br>FV:	Floating Village Residential<br>I:	Industrial<br>RH:	Residential High Density<br>RL:	Residential Low Density<br>RP:	Residential Low Density Park <br>RM:	Residential Medium Density|类别较少，独热编码|
|LotFrontage| Linear feet of street connected to property 房子同街道之间的距离|21-59-69-80-313|
|LotArea| Lot size in square feet 建筑面积|1300-7553.5-9478.5-11601.5-215245|
|Street| Type of road access 主路的路面类型|Grvl:Gravel 碎石<br>Pave:Paved|类别较少，独热编码|
|Alley| Type of alley access 小道的路面类型|Grvl:Gravel<br>Pave:Paved<br>    NA:No alley access|类别较少，独热编码|
|LotShape| General shape of property 房屋外形|Reg:Regular<br>IR1:Slightly irregular<br>IR2:Moderately Irregular<br>IR3:Irregular|类别较少，独热编码|类别较少，独热编码|
|LandContour| Flatness of the property 平整度|Lvl:Near Flat/Level	<br>Bnk:Banked - Quick and significant rise from street grade to building<br>HLS:Hillside - Significant slope from side to side<br>Low:Depression|类别较少，独热编码|
|Utilities| Type of utilities available 配套公用设施类型|AllPub:	All public Utilities (E,G,W,& S)	<br>NoSewr:	Electricity, Gas, and Water (Septic Tank)<br>NoSeWa:	Electricity and Gas Only<br>ELO:	Electricity only	|类别较少，独热编码|
|LotConfig| Lot configuration 配置|Inside:Inside lot<br>Corner:	Corner lot街角 <br>CulDSac:	Cul-de-sac  死胡同<br>FR2:	Frontage on 2 sides of property       两侧临街<br>FR3:	Frontage on 3 sides of property       三侧临街|类别较少，独热编码|
|LandSlope| Slope of property 土地坡度|Gtl:	Gentle slope<br>Mod:	Moderate Slope	<br>Sev:	Severe Slope|类别较少，独热编码|
|Neighborhood| Physical locations within Ames city limits 房屋在埃姆斯市的位置|Blmngtn:	Bloomington Heights<br>Blueste:	Bluestem<br>BrDale:	Briardale<br>BrkSide:	Brookside<br>ClearCr:	Clear Creek<br>CollgCr:	College Creek<br>Crawfor:	Crawford<br>Edwards:	Edwards<br>Gilbert:	Gilbert<br>IDOTRR:	Iowa DOT and Rail Road<br>MeadowV:	Meadow Village<br>Mitchel:	Mitchell<br>Names:	North Ames<br>NoRidge:	Northridge<br>NPkVill:	Northpark Villa<br>NridgHt:	Northridge Heights<br>NWAmes:	Northwest Ames<br>OldTown:	Old Town<br>SWISU:	South & West of Iowa State University<br>Sawyer:	Sawyer<br>SawyerW:	Sawyer West<br>Somerst:	Somerset<br>StoneBr:	Stone Brook<br>Timber:	Timberland<br>Veenker:	Veenker|
|Condition1| Proximity to main road or railroad 附近交通情况|       Artery:Adjacent to arterial street<br>Feedr:Adjacent to feeder street	<br>Norm:Normal	<br>RRNn:Within 200' of North-South Railroad<br>RRAn:Adjacent to North-South Railroad<br>PosN:Near positive off-site feature--park, greenbelt, etc.<br>PosA:Adjacent to postive off-site feature<br>RRNe:Within 200' of East-West Railroad<br>RRAe:Adjacent to East-West Railroad|
|Condition2| Proximity to main road or railroad (if a second is present) 附近交通情况（如果同时满足两种情况）|Artery:	Adjacent to arterial street<br>Feedr:	Adjacent to feeder street	<br>Norm:	Normal	<br>RRNn:	Within 200' of North-South Railroad<br>RRAn:	Adjacent to North-South Railroad<br>PosN:	Near positive off-site feature--park, greenbelt, etc.<br>PosA:	Adjacent to postive off-site feature<br>RRNe:	Within 200' of East-West Railroad<br>RRAe:	Adjacent to East-West Railroad|
|BldgType| Type of dwelling 住宅类型| 1Fam: Single-family Detached 独栋	<br>2FmCon:	Two-family Conversion; originally built as one-family dwelling 独立双户住房 <br>Duplx:Duplex 复式 <br>TwnhsE:	Townhouse End Unit 联排别墅边户 <br>TwnhsI:	Townhouse Inside Unit 联排别墅里户|类别较少，独热编码|
|HouseStyle| Style of dwelling 房屋的层数|1Story:	One story<br>1.5Fin:	One and one-half story: 2nd level finished<br>1.5Unf:	One and one-half story: 2nd level unfinished<br>2Story:	Two story<br>2.5Fin:	Two and one-half story: 2nd level finished<br>2.5Unf:	Two and one-half story: 2nd level unfinished<br>SFoyer:	Split Foyer<br>SLvl	:Split Level|
|OverallQual| Overall material and finish quality 完工质量和材料|10:	Very Excellent<br>9:	Excellent<br>8:	Very Good<br>7:	Good<br>6:	Above Average<br>5:	Average<br>4:	Below Average<br>3:	Fair<br>2:	Poor<br>1:	Very Poor|顺序变量|
|OverallCond| Overall condition rating 整体条件等级|10:	Very Excellent<br>9:	Excellent<br>8:	Very Good<br>7:	Good<br>6:	Above Average<br>5:	Average<br>4:	Below Average<br>3:	Fair<br>2:	Poor<br>1:	Very Poor|顺序变量|
|YearBuilt| Original construction date 建造年份|1875-2010,1879-2010(test)|
|YearRemodAdd| Remodel date 翻修年份|1950-2010(both)|翻修年份需大于等于建造年份|
|RoofStyle| Type of roof 屋顶类型| Flat:Flat平顶 <br>Gable:	Gable 尖顶 <br>Gambrel:	Gabrel (Barn) 复折屋顶<br>Hip	:Hip<br>Mansard:	Mansard双重斜坡的屋顶<br>Shed:	Shed|
|RoofMatl| Roof material 屋顶材料| ClyTile:Clay or Tile<br>CompShg:Standard (Composite) Shingle<br>Membran:Membrane<br>Metal:Metal<br>Roll:Roll<br>Tar&Grv:Gravel & Tar<br>WdShake:Wood Shakes<br>WdShngl:Wood Shingles	|
|Exterior1st| Exterior covering on house 外立面材料|AsbShng:	Asbestos Shingles 石棉瓦<br>AsphShn:	Asphalt Shingles<br>BrkComm:	Brick Common<br>BrkFace:	Brick Face<br>CBlock:	Cinder Block<br>CemntBd:	Cement Board<br>HdBoard:	Hard Board<br>ImStucc:	Imitation Stucco<br>MetalSd:	Metal Siding<br>Other:	Other<br>Plywood:	Plywood<br>PreCast:	PreCast	<br>Stone:	Stone<br>Stucco:	Stucco<br>VinylSd:	Vinyl Siding<br>Wd :Sdng	Wood Siding<br>WdShing	:Wood Shingles|
|Exterior2nd| Exterior covering on house (if more than one material) 外立面材料2|AsbShng:	Asbestos Shingles<br>AsphShn:	Asphalt Shingles<br>BrkComm:	Brick Common<br>BrkFace:	Brick Face<br>CBlock:	Cinder Block<br>CemntBd:	Cement Board<br>HdBoard:	Hard Board<br>ImStucc:	Imitation Stucco<br>MetalSd:	Metal Siding<br>Other:	Other<br>Plywood:	Plywood<br>PreCast:	PreCast	<br>Stone:	Stone<br>Stucco:	Stucco<br>VinylSd:	Vinyl Siding<br>Wd :Sdng	Wood Siding<br>WdShing	:Wood Shingles|
|MasVnrType| Masonry veneer type 装饰石材类型| BrkCmn:	Brick Common<br>BrkFace:	Brick Face<br>CBlock:	Cinder Block<br>None:	None<br>Stone:	Stone|
|MasVnrArea| Masonry veneer area in square feet 装饰石材面积|0-0-0-166-1660|偏态|
|ExterQual| Exterior material quality 外立面材料质量|Ex:	Excellent<br> Gd:	Good<br> TA:	Average/Typical<br> Fa:	Fair<br> Po:	Poor|顺序变量|
|ExterCond| Present condition of the material on the exterior 外立面材料外观情况|Ex:	Excellent<br> Gd:	Good<br> TA:	Average/Typical<br> Fa:	Fair<br> Po:	Poor|顺序变量|
|Foundation| Type of foundation 房屋结构类型| BrkTil:	Brick & Tile 砖和瓦片<br>CBlock:	Cinder Block 煤渣砌块 <br>PConc:	Poured Contrete	混凝土<br>Slab:	Slab<br>Stone:	Stone<br>Wood:	Wood|
|BsmtQual| Height of the basement 评估地下室层高情况| Ex:	Excellent (100+ inches)	<br>Gd:	Good (90-99 inches)<br>TA:	Typical (80-89 inches)<br>Fa:	Fair (70-79 inches)<br>Po:	Poor (<70 inches<br>NA:	No Basement|顺序变量|
|BsmtCond| General condition of the basement 地下室总体情况|        Ex:	Excellent<br>Gd:	Good<br>TA:	Typical - slight dampness allowed<br>Fa:	Fair - dampness or some cracking or settling<br>Po:	Poor - Severe cracking, settling, or wetness<br>NA:	No Basement|顺序变量|
|BsmtExposure| Walkout or garden level basement walls 地下室出口或者花园层的墙面| Gd:	Good Exposure<br>Av:	Average Exposure (split levels or foyers typically score average or above)	<br>Mn:	Mimimum Exposure<br>No:	No Exposure<br>NA:	No Basement|
|BsmtFinType1| Quality of basement finished area 地下室区域质量| GLQ:	Good Living Quarters<br>ALQ:Average Living Quarters<br>BLQ:Below Average Living Quarters	<br>Rec:Average Rec Room<br>LwQ:Low Quality<br>Unf:Unfinshed<br>NA:No Basement|
|BsmtFinSF1| Type 1 finished square feet Type 1完工面积|0-0-383.5-712.25-5644|
|BsmtFinType2| Quality of second finished area (if present) 二次完工面积质量（如果有）| GLQ:	Good Living Quarters<br>ALQ:Average Living Quarters<br>BLQ:Below Average Living Quarters	<br>Rec:Average Rec Room<br>LwQ:Low Quality<br>Unf:Unfinshed<br>NA:No Basement|
|BsmtFinSF2| Type 2 finished square feet Type 2完工面积|0-0-0-0-1474|
|BsmtUnfSF| Unfinished square feet of basement area 地下室区域未完工面积|0-223-477.5-808-2336|
|TotalBsmtSF| Total square feet of basement area 地下室总体面积|0-795.75-991.5-1298.25-6110|
|Heating| Type of heating 采暖类型| Floor:	Floor Furnace<br>GasA	:Gas forced warm air furnace<br>GasW	:Gas hot water or steam heat<br>Grav	:Gravity furnace	<br>OthW	:Hot water or steam heat other than gas<br>Wall	:Wall furnace|
|HeatingQC| Heating quality and condition 采暖质量和条件|       Ex:	Excellent<br>Gd:	Good<br>TA:	Average/Typical<br>Fa:	Fair<br>Po:	Poor|顺序变量|
|CentralAir| Central air conditioning 中央空调系统|N: No; Y: yes|
|Electrical| Electrical system 电力系统|SBrkr:	Standard Circuit Breakers & Romex<br>FuseA:	Fuse Box over 60 AMP and all Romex wiring (Average)	<br>FuseF:	60 AMP Fuse Box and mostly Romex wiring (Fair)<br>FuseP: 60 AMP Fuse Box and mostly knob & tube wiring (poor)<br>Mix	:Mixed|
|1stFlrSF| First Floor square feet 第一层面积|334-882-1087-1391.25-4692| 后1/4很大
|2ndFlrSF| Second floor square feet 第二层面积|0-0-0-728-2065|
|LowQualFinSF| Low quality finished square feet (all floors) 低质量完工面积|0-0-0-0-572|要提取个标签吗|
|GrLivArea| Above grade (ground) living area square feet 地面以上部分起居面积|334-1129.5-1464-1776.75-5642|
|BsmtFullBath| Basement full bathrooms 地下室全浴室数量|0, 1, 2, 3|
|BsmtHalfBath| Basement half bathrooms 地下室半浴室数量|0, 1, 2|
|FullBath| Full bathrooms above grade 地面以上全浴室数量|0, 1, 2, 3|
|HalfBath| Half baths above grade 地面以上半浴室数量|0, 1, 2|
|BedroomAbvGr| Number of bedrooms above basement level (does NOT include basement bedrooms) 地面以上卧室数量|0, 1, 2, 3, 4, 5, 6, 8|
|KitchenAbvGr| Number of kitchens 厨房数量|0, 1, 2|
|KitchenQual| Kitchen quality 厨房质量|Ex:	Excellent<br>Gd:	Good<br>TA:	Average/Typical<br>Fa:	Fair<br>Po:	Poor|顺序变量|
|TotRmsAbvGrd| Total rooms above grade (does not include bathrooms) 总房间数（不含浴室和地下部分）|3-15|这里可以计算下有没有异常值|
|Functional| Home functionality rating 功能性评级| Typ:	Typical Functionality<br>Min1:	Minor Deductions 1<br>Min2:	Minor Deductions 2<br>Mod:	Moderate Deductions<br>Maj1:	Major Deductions 1<br>Maj2:	Major Deductions 2<br>Sev:	Severely Damaged<br>Sal:	Salvage only|
|Fireplaces| Number of fireplaces 壁炉数量|0-4|
|FireplaceQu| Fireplace quality 壁炉质量| Ex:	Excellent - Exceptional Masonry Fireplace<br>Gd:	Good - Masonry Fireplace in main level<br>TA:	Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement<br>Fa:	Fair - Prefabricated Fireplace in basement<br>Po:	Poor - Ben Franklin Stove<br>NA:	No Fireplace|顺序变量|
|GarageType| Garage location 车库位置|       2Types:	More than one type of garage<br>Attchd:	Attached to home<br>Basment:	Basement Garage<br>BuiltIn:	Built-In (Garage part of house - typically has room above garage)<br>CarPort:	Car Port<br>Detchd:	Detached from home<br>NA:	No Garage|
|GarageYrBlt| Year garage was built 车库建造时间|1895-2010|有个2207异常值需要修复; 转成int; 可以计算与房屋建造的时间差后判断是否newer｜
|GarageFinish| Interior finish of the garage 车库内饰|Fin:	Finished<br>RFn:	Rough Finished	<br>Unf:	Unfinished<br>NA:	No Garage|
|GarageCars| Size of garage in car capacity 车壳大小以停车数量表示|0-5|
|GarageArea| Size of garage in square feet 车库面积|0-334.5-480-576-1418|
|GarageQual| Garage quality 车库质量|Ex:	Excellent<br>Gd:	Good<br>TA:	Average/Typical<br>Fa:	Fair<br>Po:	Poor|顺序变量|
|GarageCond| Garage condition 车库条件|Ex:	Excellent<br>Gd:	Good<br>TA:	Average/Typical<br>Fa:	Fair<br>Po:	Poor|顺序变量|
|PavedDrive| Paved driveway 车道铺砌情况| Y:	Paved ; P:	Partial Pavement; N:	Dirt/Gravel|
|WoodDeckSF| Wood deck area in square feet 实木地板面积|0-0-0-168-857|
|OpenPorchSF| Open porch area in square feet 开放式门廊面积|0-0-25-68-547|
|EnclosedPorch| Enclosed porch area in square feet 封闭式门廊面积|0-0-0-0-552|
|3SsnPorch| Three season porch area in square feet 时令门廊面积|0-0-0-0-508|
|ScreenPorch| Screen porch area in square feet 屏风门廊面积|0-0-0-0-480|
|PoolArea| Pool area in square feet 游泳池面积|0-0-0-0-738|
|PoolQC| Pool quality 游泳池质量|Ex:	Excellent<br>Gd:	Good<br>TA:	Average/Typical<br>Fa:	Fair<br>Po:	Poor|顺序变量|
|Fence| Fence quality 围栏质量|GdPrv:	Good Privacy<br>MnPrv:	Minimum Privacy<br>GdWo:	Good Wood<br>MnWw:	Minimum Wood/Wire<br>NA	:No Fence|
|MiscFeature| Miscellaneous feature not covered in other categories 其它条件中未包含部分的特性|Elev:	Elevator<br> Gar2:	2nd Garage (if not described in garage section)<br> Othr:	Other<br> Shed:	Shed (over 100 SF)<br> TenC:	Tennis Court<br> NA	:None|
|MiscVal| $Value of miscellaneous feature 杂项部分价值|0-0-0-0-15500|
|MoSold| Month Sold 卖出月份|1-12|
|YrSold| Year Sold 卖出年份|2006-2010|计算与建造的年份差|
|SaleType| Type of sale 出售类型|WD :Warranty Deed - Conventional<br>CWD	:Warranty Deed - Cash<br>VWD	:Warranty Deed - VA Loan<br>New	:Home just constructed and sold<br>COD	:Court Officer Deed/Estate<br>Con	:Contract 15% Down payment regular terms<br>ConLw:	Contract Low Down payment and low interest<br>ConLI:	Contract Low Interest<br>ConLD:	Contract Low Down<br>Oth	:Other|
|SaleCondition| Condition of sale 出售条件|Normal:Normal Sale<br>Abnorml:	Abnormal Sale -  trade, foreclosure, short sale<br>AdjLand:	Adjoining Land Purchase<br>Alloca:	Allocation - two linked properties with separate deeds, typically condo with a garage unit	<br>Family:	Sale between family members<br>Partial:	Home was not completed when last assessed (associated with New Homes)|