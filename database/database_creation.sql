CREATE SCHEMA tohumschema;

SET
search_path TO tohumschema;

CREATE TABLE region
(
    RegionID   integer,
    RegionName varchar(30),
    PRIMARY KEY (RegionID)
);

CREATE TABLE city
(
    RegionID integer,
    CityID   integer,
    CityName varchar(15),
    PRIMARY KEY (CityID),
    FOREIGN KEY (RegionID) REFERENCES region (RegionID)
);

CREATE TABLE farmer
(
    FarmerID serial,
    Mail     varchar(50) unique,
    Name     varchar(20),
    Lastname varchar(30),
    Password varchar(20),
    CityID   integer,
    PRIMARY KEY (FarmerID),
    FOREIGN KEY (CityID) REFERENCES city (CityID)
);

CREATE TABLE product
(
    ProductID   serial,
    Name        varchar(20),
    Type        integer NOT NULL,
    Coefficient integer DEFAULT 0,
    RegionID    integer,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (RegionID) REFERENCES region (RegionID)
);

CREATE TABLE opposite
(
    ProductID         integer,
    OppositeProductID integer,
    PRIMARY KEY (ProductID, OppositeProductID),
    FOREIGN KEY (ProductID) REFERENCES product (ProductID),
    FOREIGN KEY (OppositeProductID) REFERENCES product (ProductID)
);

CREATE TABLE data
(
    DataID         serial,
    FarmerID       integer,
    MedicineAmount integer,
    MachineAmount  integer,
    WorkerAmount   integer,
    Year           integer CHECK ( Year > 1950
) ,
    PRIMARY KEY (DataID),
    FOREIGN KEY (FarmerID) REFERENCES farmer (FarmerID)
);

CREATE TABLE productdata
(
    ProductataID serial,
    DataID       integer,
    ProductID    integer,
    FarmerID     integer,
    Area         integer,
    Ton          integer,
    Year         integer CHECK ( Year > 1950
) ,
    PRIMARY KEY (DataID),
    FOREIGN KEY (DataID) REFERENCES data (DataID),
    FOREIGN KEY (ProductID) REFERENCES product (ProductID),
    FOREIGN KEY (FarmerID) REFERENCES farmer (FarmerID),
    FOREIGN KEY (DataID) REFERENCES data (DataID)
);

CREATE TABLE growing
(
    GrowId      serial,
    FarmerId    integer,
    ProductId   integer,
    Area        integer,
    SeedDate    date,
    HarvestDate date,
    Status      varchar(15),
    PRIMARY KEY (GrowId),
    FOREIGN KEY (FarmerId) REFERENCES farmer (FarmerId),
    FOREIGN KEY (ProductId) REFERENCES product (ProductId)
);

CREATE TABLE systemlog
(
    LogId       serial,
    FarmerId    integer,
    OperType    varchar(15),
    LogDateTime timestamp,
    PRIMARY KEY (LogId),
    FOREIGN KEY (FarmerId) REFERENCES farmer (FarmerId)
);