CREATE TABLE favoritePointReason (
    userId VARCHAR2(12) NOT NULL,
    pointReasonNo NUMBER(3) NOT NULL,

    CONSTRAINT pk_favoritePointReason PRIMARY KEY (userId, pointReasonNo),

    CONSTRAINT fk_fav_user FOREIGN KEY (userId) 
        REFERENCES users(id) ON DELETE CASCADE,

    CONSTRAINT fk_fav_pointReason FOREIGN KEY (pointReasonNo) 
        REFERENCES pointReason(no) ON DELETE CASCADE
);