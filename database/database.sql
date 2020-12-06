--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.25
-- Dumped by pg_dump version 9.3.25
-- Started on 2020-12-05 21:42:51 +03

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 1 (class 3079 OID 11791)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2171 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 189 (class 1259 OID 24944)
-- Name: bakliyat; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.bakliyat (
    bakliyatid integer NOT NULL
);


ALTER TABLE public.bakliyat OWNER TO postgres;

--
-- TOC entry 188 (class 1259 OID 24942)
-- Name: bakliyat_bakliyatid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bakliyat_bakliyatid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bakliyat_bakliyatid_seq OWNER TO postgres;

--
-- TOC entry 2172 (class 0 OID 0)
-- Dependencies: 188
-- Name: bakliyat_bakliyatid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bakliyat_bakliyatid_seq OWNED BY public.bakliyat.bakliyatid;


--
-- TOC entry 194 (class 1259 OID 25007)
-- Name: barindirir; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.barindirir (
    ciftciid integer NOT NULL,
    ilceid integer NOT NULL
);


ALTER TABLE public.barindirir OWNER TO postgres;

--
-- TOC entry 192 (class 1259 OID 25003)
-- Name: barindirir_ciftciid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.barindirir_ciftciid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.barindirir_ciftciid_seq OWNER TO postgres;

--
-- TOC entry 2173 (class 0 OID 0)
-- Dependencies: 192
-- Name: barindirir_ciftciid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.barindirir_ciftciid_seq OWNED BY public.barindirir.ciftciid;


--
-- TOC entry 193 (class 1259 OID 25005)
-- Name: barindirir_ilceid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.barindirir_ilceid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.barindirir_ilceid_seq OWNER TO postgres;

--
-- TOC entry 2174 (class 0 OID 0)
-- Dependencies: 193
-- Name: barindirir_ilceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.barindirir_ilceid_seq OWNED BY public.barindirir.ilceid;


--
-- TOC entry 175 (class 1259 OID 24873)
-- Name: bolge; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.bolge (
    bolgeid integer NOT NULL,
    bolgename character varying(25)
);


ALTER TABLE public.bolge OWNER TO postgres;

--
-- TOC entry 174 (class 1259 OID 24871)
-- Name: bolge_bolgeid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bolge_bolgeid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bolge_bolgeid_seq OWNER TO postgres;

--
-- TOC entry 2175 (class 0 OID 0)
-- Dependencies: 174
-- Name: bolge_bolgeid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bolge_bolgeid_seq OWNED BY public.bolge.bolgeid;


--
-- TOC entry 203 (class 1259 OID 25092)
-- Name: bulundurur; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.bulundurur (
    veriid integer NOT NULL,
    ilid integer NOT NULL
);


ALTER TABLE public.bulundurur OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 25090)
-- Name: bulundurur_ilid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bulundurur_ilid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bulundurur_ilid_seq OWNER TO postgres;

--
-- TOC entry 2176 (class 0 OID 0)
-- Dependencies: 202
-- Name: bulundurur_ilid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bulundurur_ilid_seq OWNED BY public.bulundurur.ilid;


--
-- TOC entry 201 (class 1259 OID 25088)
-- Name: bulundurur_veriid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bulundurur_veriid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bulundurur_veriid_seq OWNER TO postgres;

--
-- TOC entry 2177 (class 0 OID 0)
-- Dependencies: 201
-- Name: bulundurur_veriid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bulundurur_veriid_seq OWNED BY public.bulundurur.veriid;


--
-- TOC entry 172 (class 1259 OID 24860)
-- Name: ciftci; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.ciftci (
    ciftciid integer NOT NULL,
    ciftcifname character varying(20),
    ciftcilname character varying(15),
    ciftcimail character varying(30),
    ciftcipassword character varying(20)
);


ALTER TABLE public.ciftci OWNER TO postgres;

--
-- TOC entry 171 (class 1259 OID 24858)
-- Name: ciftci_ciftciid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ciftci_ciftciid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ciftci_ciftciid_seq OWNER TO postgres;

--
-- TOC entry 2178 (class 0 OID 0)
-- Dependencies: 171
-- Name: ciftci_ciftciid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ciftci_ciftciid_seq OWNED BY public.ciftci.ciftciid;


--
-- TOC entry 177 (class 1259 OID 24881)
-- Name: il; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.il (
    ilid integer NOT NULL,
    ilname character varying(20),
    bolgeid integer
);


ALTER TABLE public.il OWNER TO postgres;

--
-- TOC entry 176 (class 1259 OID 24879)
-- Name: il_ilid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.il_ilid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.il_ilid_seq OWNER TO postgres;

--
-- TOC entry 2179 (class 0 OID 0)
-- Dependencies: 176
-- Name: il_ilid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.il_ilid_seq OWNED BY public.il.ilid;


--
-- TOC entry 179 (class 1259 OID 24889)
-- Name: ilce; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.ilce (
    ilceid integer NOT NULL,
    ilcename character varying(20),
    bolgeid integer,
    ilid integer
);


ALTER TABLE public.ilce OWNER TO postgres;

--
-- TOC entry 178 (class 1259 OID 24887)
-- Name: ilce_ilceid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ilce_ilceid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ilce_ilceid_seq OWNER TO postgres;

--
-- TOC entry 2180 (class 0 OID 0)
-- Dependencies: 178
-- Name: ilce_ilceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ilce_ilceid_seq OWNED BY public.ilce.ilceid;


--
-- TOC entry 183 (class 1259 OID 24905)
-- Name: meyve; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.meyve (
    meyveid integer NOT NULL
);


ALTER TABLE public.meyve OWNER TO postgres;

--
-- TOC entry 182 (class 1259 OID 24903)
-- Name: meyve_meyveid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.meyve_meyveid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.meyve_meyveid_seq OWNER TO postgres;

--
-- TOC entry 2181 (class 0 OID 0)
-- Dependencies: 182
-- Name: meyve_meyveid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.meyve_meyveid_seq OWNED BY public.meyve.meyveid;


--
-- TOC entry 185 (class 1259 OID 24918)
-- Name: sebze; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.sebze (
    sebzeid integer NOT NULL
);


ALTER TABLE public.sebze OWNER TO postgres;

--
-- TOC entry 184 (class 1259 OID 24916)
-- Name: sebze_sebzeid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sebze_sebzeid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sebze_sebzeid_seq OWNER TO postgres;

--
-- TOC entry 2182 (class 0 OID 0)
-- Dependencies: 184
-- Name: sebze_sebzeid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sebze_sebzeid_seq OWNED BY public.sebze.sebzeid;


--
-- TOC entry 187 (class 1259 OID 24931)
-- Name: tahil; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.tahil (
    tahilid integer NOT NULL
);


ALTER TABLE public.tahil OWNER TO postgres;

--
-- TOC entry 186 (class 1259 OID 24929)
-- Name: tahil_tahilid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tahil_tahilid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tahil_tahilid_seq OWNER TO postgres;

--
-- TOC entry 2183 (class 0 OID 0)
-- Dependencies: 186
-- Name: tahil_tahilid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tahil_tahilid_seq OWNED BY public.tahil.tahilid;


--
-- TOC entry 173 (class 1259 OID 24866)
-- Name: ulke; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.ulke (
    ulkename character varying(20) NOT NULL
);


ALTER TABLE public.ulke OWNER TO postgres;

--
-- TOC entry 181 (class 1259 OID 24897)
-- Name: urun; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.urun (
    urunid integer NOT NULL,
    urunname character varying(20),
    urunkatsayi character varying(20)
);


ALTER TABLE public.urun OWNER TO postgres;

--
-- TOC entry 180 (class 1259 OID 24895)
-- Name: urun_urunid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.urun_urunid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.urun_urunid_seq OWNER TO postgres;

--
-- TOC entry 2184 (class 0 OID 0)
-- Dependencies: 180
-- Name: urun_urunid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.urun_urunid_seq OWNED BY public.urun.urunid;


--
-- TOC entry 191 (class 1259 OID 24957)
-- Name: veri; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.veri (
    veriid integer NOT NULL,
    toplamilacmiktari integer,
    toplammakinesayisi integer,
    iscisayisi integer,
    yil integer NOT NULL,
    CONSTRAINT veri_yil_check CHECK (((yil >= 1950) AND (yil <= 2020)))
);


ALTER TABLE public.veri OWNER TO postgres;

--
-- TOC entry 190 (class 1259 OID 24955)
-- Name: veri_veriid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.veri_veriid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.veri_veriid_seq OWNER TO postgres;

--
-- TOC entry 2185 (class 0 OID 0)
-- Dependencies: 190
-- Name: veri_veriid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.veri_veriid_seq OWNED BY public.veri.veriid;


--
-- TOC entry 197 (class 1259 OID 25049)
-- Name: yetisir; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.yetisir (
    bolgeid integer NOT NULL,
    ilceid integer NOT NULL,
    ton integer,
    alan integer,
    yil integer NOT NULL,
    CONSTRAINT yetisir_yil_check CHECK (((yil >= 1950) AND (yil <= 2020)))
);


ALTER TABLE public.yetisir OWNER TO postgres;

--
-- TOC entry 195 (class 1259 OID 25045)
-- Name: yetisir_bolgeid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.yetisir_bolgeid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yetisir_bolgeid_seq OWNER TO postgres;

--
-- TOC entry 2186 (class 0 OID 0)
-- Dependencies: 195
-- Name: yetisir_bolgeid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.yetisir_bolgeid_seq OWNED BY public.yetisir.bolgeid;


--
-- TOC entry 196 (class 1259 OID 25047)
-- Name: yetisir_ilceid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.yetisir_ilceid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.yetisir_ilceid_seq OWNER TO postgres;

--
-- TOC entry 2187 (class 0 OID 0)
-- Dependencies: 196
-- Name: yetisir_ilceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.yetisir_ilceid_seq OWNED BY public.yetisir.ilceid;


--
-- TOC entry 200 (class 1259 OID 25071)
-- Name: zitlasir; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE public.zitlasir (
    firsturunid integer NOT NULL,
    secondurunid integer NOT NULL
);


ALTER TABLE public.zitlasir OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 25067)
-- Name: zitlasir_firsturunid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.zitlasir_firsturunid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.zitlasir_firsturunid_seq OWNER TO postgres;

--
-- TOC entry 2188 (class 0 OID 0)
-- Dependencies: 198
-- Name: zitlasir_firsturunid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.zitlasir_firsturunid_seq OWNED BY public.zitlasir.firsturunid;


--
-- TOC entry 199 (class 1259 OID 25069)
-- Name: zitlasir_secondurunid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.zitlasir_secondurunid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.zitlasir_secondurunid_seq OWNER TO postgres;

--
-- TOC entry 2189 (class 0 OID 0)
-- Dependencies: 199
-- Name: zitlasir_secondurunid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.zitlasir_secondurunid_seq OWNED BY public.zitlasir.secondurunid;


--
-- TOC entry 1963 (class 2604 OID 24947)
-- Name: bakliyatid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bakliyat ALTER COLUMN bakliyatid SET DEFAULT nextval('public.bakliyat_bakliyatid_seq'::regclass);


--
-- TOC entry 1966 (class 2604 OID 25010)
-- Name: ciftciid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.barindirir ALTER COLUMN ciftciid SET DEFAULT nextval('public.barindirir_ciftciid_seq'::regclass);


--
-- TOC entry 1967 (class 2604 OID 25011)
-- Name: ilceid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.barindirir ALTER COLUMN ilceid SET DEFAULT nextval('public.barindirir_ilceid_seq'::regclass);


--
-- TOC entry 1956 (class 2604 OID 24876)
-- Name: bolgeid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bolge ALTER COLUMN bolgeid SET DEFAULT nextval('public.bolge_bolgeid_seq'::regclass);


--
-- TOC entry 1973 (class 2604 OID 25095)
-- Name: veriid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bulundurur ALTER COLUMN veriid SET DEFAULT nextval('public.bulundurur_veriid_seq'::regclass);


--
-- TOC entry 1974 (class 2604 OID 25096)
-- Name: ilid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bulundurur ALTER COLUMN ilid SET DEFAULT nextval('public.bulundurur_ilid_seq'::regclass);


--
-- TOC entry 1955 (class 2604 OID 24863)
-- Name: ciftciid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ciftci ALTER COLUMN ciftciid SET DEFAULT nextval('public.ciftci_ciftciid_seq'::regclass);


--
-- TOC entry 1957 (class 2604 OID 24884)
-- Name: ilid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.il ALTER COLUMN ilid SET DEFAULT nextval('public.il_ilid_seq'::regclass);


--
-- TOC entry 1958 (class 2604 OID 24892)
-- Name: ilceid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ilce ALTER COLUMN ilceid SET DEFAULT nextval('public.ilce_ilceid_seq'::regclass);


--
-- TOC entry 1960 (class 2604 OID 24908)
-- Name: meyveid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meyve ALTER COLUMN meyveid SET DEFAULT nextval('public.meyve_meyveid_seq'::regclass);


--
-- TOC entry 1961 (class 2604 OID 24921)
-- Name: sebzeid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sebze ALTER COLUMN sebzeid SET DEFAULT nextval('public.sebze_sebzeid_seq'::regclass);


--
-- TOC entry 1962 (class 2604 OID 24934)
-- Name: tahilid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tahil ALTER COLUMN tahilid SET DEFAULT nextval('public.tahil_tahilid_seq'::regclass);


--
-- TOC entry 1959 (class 2604 OID 24900)
-- Name: urunid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.urun ALTER COLUMN urunid SET DEFAULT nextval('public.urun_urunid_seq'::regclass);


--
-- TOC entry 1964 (class 2604 OID 24960)
-- Name: veriid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.veri ALTER COLUMN veriid SET DEFAULT nextval('public.veri_veriid_seq'::regclass);


--
-- TOC entry 1968 (class 2604 OID 25052)
-- Name: bolgeid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.yetisir ALTER COLUMN bolgeid SET DEFAULT nextval('public.yetisir_bolgeid_seq'::regclass);


--
-- TOC entry 1969 (class 2604 OID 25053)
-- Name: ilceid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.yetisir ALTER COLUMN ilceid SET DEFAULT nextval('public.yetisir_ilceid_seq'::regclass);


--
-- TOC entry 1971 (class 2604 OID 25074)
-- Name: firsturunid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.zitlasir ALTER COLUMN firsturunid SET DEFAULT nextval('public.zitlasir_firsturunid_seq'::regclass);


--
-- TOC entry 1972 (class 2604 OID 25075)
-- Name: secondurunid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.zitlasir ALTER COLUMN secondurunid SET DEFAULT nextval('public.zitlasir_secondurunid_seq'::regclass);


--
-- TOC entry 2148 (class 0 OID 24944)
-- Dependencies: 189
-- Data for Name: bakliyat; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bakliyat (bakliyatid) FROM stdin;
\.


--
-- TOC entry 2190 (class 0 OID 0)
-- Dependencies: 188
-- Name: bakliyat_bakliyatid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bakliyat_bakliyatid_seq', 1, false);


--
-- TOC entry 2153 (class 0 OID 25007)
-- Dependencies: 194
-- Data for Name: barindirir; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.barindirir (ciftciid, ilceid) FROM stdin;
\.


--
-- TOC entry 2191 (class 0 OID 0)
-- Dependencies: 192
-- Name: barindirir_ciftciid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.barindirir_ciftciid_seq', 1, false);


--
-- TOC entry 2192 (class 0 OID 0)
-- Dependencies: 193
-- Name: barindirir_ilceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.barindirir_ilceid_seq', 1, false);


--
-- TOC entry 2134 (class 0 OID 24873)
-- Dependencies: 175
-- Data for Name: bolge; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bolge (bolgeid, bolgename) FROM stdin;
1	Akdeniz Bölgesi
2	Doğu Anadolu Bölgesi
3	Ege Bölgesi
4	Güneydoğu Anadolu Bölgesi
5	İç Anadolu Bölgesi
6	Karadeniz Bölgesi
7	Marmara Bölgesi
\.


--
-- TOC entry 2193 (class 0 OID 0)
-- Dependencies: 174
-- Name: bolge_bolgeid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bolge_bolgeid_seq', 1, false);


--
-- TOC entry 2162 (class 0 OID 25092)
-- Dependencies: 203
-- Data for Name: bulundurur; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bulundurur (veriid, ilid) FROM stdin;
\.


--
-- TOC entry 2194 (class 0 OID 0)
-- Dependencies: 202
-- Name: bulundurur_ilid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bulundurur_ilid_seq', 1, false);


--
-- TOC entry 2195 (class 0 OID 0)
-- Dependencies: 201
-- Name: bulundurur_veriid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bulundurur_veriid_seq', 1, false);


--
-- TOC entry 2131 (class 0 OID 24860)
-- Dependencies: 172
-- Data for Name: ciftci; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ciftci (ciftciid, ciftcifname, ciftcilname, ciftcimail, ciftcipassword) FROM stdin;
\.


--
-- TOC entry 2196 (class 0 OID 0)
-- Dependencies: 171
-- Name: ciftci_ciftciid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ciftci_ciftciid_seq', 1, false);


--
-- TOC entry 2136 (class 0 OID 24881)
-- Dependencies: 177
-- Data for Name: il; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.il (ilid, ilname, bolgeid) FROM stdin;
1	Adana	1
2	Adiyaman	4
3	Afyonkarahisar	3
4	Agri	2
5	Amasya	6
6	Ankara	5
7	Antalya	1
8	Artvin	6
9	Aydin	3
10	Balikesir	7
11	Bilecik	7
12	Bingol	2
13	Bitlis	2
14	Bolu	6
15	Burdur	1
16	Bursa	7
17	Canakkale	7
18	Cankiri	5
19	Corum	6
20	Denizli	3
21	Diyarbakir	4
22	Edirne	7
23	Elazig	2
24	Erzincan	2
25	Erzurum	2
26	Eskisehir	5
27	Gaziantep	4
28	Giresun	6
29	Gumushane	6
30	Hakkari	2
31	Hatay	1
32	Isparta	1
33	Mersin	1
34	Istanbul	7
35	Izmir	3
36	Kars	2
37	Kastamonu	6
38	Kayseri	5
39	Kirklareli	7
40	Kirsehir	5
41	Kocaeli	7
42	Konya	5
43	Kutahya	3
44	Malatya	2
45	Manisa	3
46	Kahramanmaras	1
47	Mardin	4
48	Mugla	3
49	Mus	2
50	NevSehir	5
51	Nigde	5
52	Ordu	6
53	Rize	6
54	Sakarya	7
55	Samsun	6
56	Siirt	4
57	Sinop	6
58	Sivas	5
59	Tekirdag	7
60	Tokat	6
61	Trabzon	6
62	Tunceli	2
63	Sanliurfa	4
64	Usak	3
65	Van	2
66	Yozgat	5
67	Zonguldak	6
68	Aksaray	5
69	Bayburt	6
70	Karaman	5
71	Kirikkale	5
72	Batman	4
73	Sirnak	4
74	Bartin	6
75	Ardahan	2
76	Igdir	2
77	Yalova	7
78	Karabuk	6
79	Kilis	4
80	Osmaniye	1
81	Duzce	6
\.


--
-- TOC entry 2197 (class 0 OID 0)
-- Dependencies: 176
-- Name: il_ilid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.il_ilid_seq', 1, false);


--
-- TOC entry 2138 (class 0 OID 24889)
-- Dependencies: 179
-- Data for Name: ilce; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ilce (ilceid, ilcename, bolgeid, ilid) FROM stdin;
1	ALADAG	1	1
2	CEYHAN	1	1
3	CUKUROVA	1	1
4	FEKE	1	1
5	IMAMOGLU	1	1
6	KARAISALI	1	1
7	KARATAS	1	1
8	KOZAN	1	1
9	POZANTI	1	1
10	SAIMBEYLI	1	1
11	SARICAM	1	1
12	SEYHAN	1	1
13	TUFANBEYLI	1	1
14	YUMURTALIK	1	1
15	YUREGIR	1	1
16	BESNI	4	2
17	CELIKHAN	4	2
18	GERGER	4	2
19	GOLBASI	4	2
20	KAHTA	4	2
21	MERKEZ	4	2
22	SAMSAT	4	2
23	SINCIK	4	2
24	TUT	4	2
25	BASMAKCI	3	3
26	BAYAT	3	3
27	BOLVADIN	3	3
28	CAY	3	3
29	COBANLAR	3	3
30	DAZKIRI	3	3
31	DINAR	3	3
32	EMIRDAG	3	3
33	EVCILER	3	3
34	HOCALAR	3	3
35	IHSANIYE	3	3
36	ISCEHISAR	3	3
37	KIZILOREN	3	3
38	MERKEZ	3	3
39	SANDIKLI	3	3
40	SINANPASA	3	3
41	SULTANDAGI	3	3
42	SUHUT	3	3
43	DIYADIN	2	4
44	DOGUBAYAZIT	2	4
45	ELESKIRT	2	4
46	HAMUR	2	4
47	MERKEZ	2	4
48	PATNOS	2	4
49	TASLICAY	2	4
50	TUTAK	2	4
51	AGACOREN	5	68
52	ESKIL	5	68
53	GULAGAC	5	68
54	GUZELYURT	5	68
55	MERKEZ	5	68
56	ORTAKOY	5	68
57	SARIYAHSI	5	68
58	SULTANHANI	5	68
59	GOYNUCEK	6	5
60	GUMUSHACIKOY	6	5
61	HAMAMOZU	6	5
62	MERKEZ	6	5
63	MERZIFON	6	5
64	SULUOVA	6	5
65	TASOVA	6	5
66	AKYURT	5	6
67	ALTINDAG	5	6
68	AYAS	5	6
69	BALA	5	6
70	BEYPAZARI	5	6
71	CAMLIDERE	5	6
72	CANKAYA	5	6
73	CUBUK	5	6
74	ELMADAG	5	6
75	ETIMESGUT	5	6
76	EVREN	5	6
77	GOLBASI	5	6
78	GUDUL	5	6
79	HAYMANA	5	6
80	KAHRAMANKAZAN	5	6
81	KALECIK	5	6
82	KECIOREN	5	6
83	KIZILCAHAMAM	5	6
84	MAMAK	5	6
85	NALLIHAN	5	6
86	POLATLI	5	6
87	PURSAKLAR	5	6
88	SINCAN	5	6
89	SEREFLIKOCHISAR	5	6
90	YENIMAHALLE	5	6
91	AKSEKI	1	7
92	AKSU	1	7
93	ALANYA	1	7
94	DEMRE	1	7
95	DOSEMEALTI	1	7
96	ELMALI	1	7
97	FINIKE	1	7
98	GAZIPASA	1	7
99	GUNDOGMUS	1	7
100	IBRADI	1	7
101	KAS	1	7
102	KEMER	1	7
103	KEPEZ	1	7
104	KONYAALTI	1	7
105	KORKUTELI	1	7
106	KUMLUCA	1	7
107	MANAVGAT	1	7
108	MURATPASA	1	7
109	SERIK	1	7
110	CILDIR	2	75
111	DAMAL	2	75
112	GOLE	2	75
113	HANAK	2	75
114	MERKEZ	2	75
115	POSOF	2	75
116	ARDANUC	6	8
117	ARHAVI	6	8
118	BORCKA	6	8
119	HOPA	6	8
120	KEMALPASA	6	8
121	MERKEZ	6	8
122	MURGUL	6	8
123	SAVSAT	6	8
124	YUSUFELI	6	8
125	BOZDOGAN	3	9
126	BUHARKENT	3	9
127	CINE	3	9
128	DIDIM	3	9
129	EFELER	3	9
130	GERMENCIK	3	9
131	INCIRLIOVA	3	9
132	KARACASU	3	9
133	KARPUZLU	3	9
134	KOCARLI	3	9
135	KOSK	3	9
136	KUSADASI	3	9
137	KUYUCAK	3	9
138	NAZILLI	3	9
139	SOKE	3	9
140	SULTANHISAR	3	9
141	YENIPAZAR	3	9
142	ALTIEYLUL	7	10
143	AYVALIK	7	10
144	BALYA	7	10
145	BANDIRMA	7	10
146	BIGADIC	7	10
147	BURHANIYE	7	10
148	DURSUNBEY	7	10
149	EDREMIT	7	10
150	ERDEK	7	10
151	GOMEC	7	10
152	GONEN	7	10
153	HAVRAN	7	10
154	IVRINDI	7	10
155	KARESI	7	10
156	KEPSUT	7	10
157	MANYAS	7	10
158	MARMARA	7	10
159	SAVASTEPE	7	10
160	SINDIRGI	7	10
161	SUSURLUK	7	10
162	AMASRA	6	74
163	KURUCASILE	6	74
164	MERKEZ	6	74
165	ULUS	6	74
166	BESIRI	4	72
167	GERCUS	4	72
168	HASANKEYF	4	72
169	KOZLUK	4	72
170	MERKEZ	4	72
171	SASON	4	72
172	AYDINTEPE	6	69
173	DEMIROZU	6	69
174	MERKEZ	6	69
175	BOZUYUK	7	11
176	GOLPAZARI	7	11
177	INHISAR	7	11
178	MERKEZ	7	11
179	OSMANELI	7	11
180	PAZARYERI	7	11
181	SOGUT	7	11
182	YENIPAZAR	7	11
183	ADAKLI	2	12
184	GENC	2	12
185	KARLIOVA	2	12
186	KIGI	2	12
187	MERKEZ	2	12
188	SOLHAN	2	12
189	YAYLADERE	2	12
190	YEDISU	2	12
191	ADILCEVAZ	2	13
192	AHLAT	2	13
193	GUROYMAK	2	13
194	HIZAN	2	13
195	MERKEZ	2	13
196	MUTKI	2	13
197	TATVAN	2	13
198	DORTDIVAN	6	14
199	GEREDE	6	14
200	GOYNUK	6	14
201	KIBRISCIK	6	14
202	MENGEN	6	14
203	MERKEZ	6	14
204	MUDURNU	6	14
205	SEBEN	6	14
206	YENICAGA	6	14
207	AGLASUN	1	15
208	ALTINYAYLA	1	15
209	BUCAK	1	15
210	CAVDIR	1	15
211	CELTIKCI	1	15
212	GOLHISAR	1	15
213	KARAMANLI	1	15
214	KEMER	1	15
215	MERKEZ	1	15
216	TEFENNI	1	15
217	YESILOVA	1	15
218	BUYUKORHAN	7	16
219	GEMLIK	7	16
220	GURSU	7	16
221	HARMANCIK	7	16
222	INEGOL	7	16
223	IZNIK	7	16
224	KARACABEY	7	16
225	KELES	7	16
226	KESTEL	7	16
227	MUDANYA	7	16
228	MUSTAFAKEMALPASA	7	16
229	NILUFER	7	16
230	ORHANELI	7	16
231	ORHANGAZI	7	16
232	OSMANGAZI	7	16
233	YENISEHIR	7	16
234	YILDIRIM	7	16
235	AYVACIK	7	17
236	BAYRAMIC	7	17
237	BIGA	7	17
238	BOZCAADA	7	17
239	CAN	7	17
240	ECEABAT	7	17
241	EZINE	7	17
242	GELIBOLU	7	17
243	GOKCEADA	7	17
244	LAPSEKI	7	17
245	MERKEZ	7	17
246	YENICE	7	17
247	ATKARACALAR	5	18
248	BAYRAMOREN	5	18
249	CERKES	5	18
250	ELDIVAN	5	18
251	ILGAZ	5	18
252	KIZILIRMAK	5	18
253	KORGUN	5	18
254	KURSUNLU	5	18
255	MERKEZ	5	18
256	ORTA	5	18
257	SABANOZU	5	18
258	YAPRAKLI	5	18
259	ALACA	6	19
260	BAYAT	6	19
261	BOGAZKALE	6	19
262	DODURGA	6	19
263	ISKILIP	6	19
264	KARGI	6	19
265	LACIN	6	19
266	MECITOZU	6	19
267	MERKEZ	6	19
268	OGUZLAR	6	19
269	ORTAKOY	6	19
270	OSMANCIK	6	19
271	SUNGURLU	6	19
272	UGURLUDAG	6	19
273	ACIPAYAM	3	20
274	BABADAG	3	20
275	BAKLAN	3	20
276	BEKILLI	3	20
277	BEYAGAC	3	20
278	BOZKURT	3	20
279	BULDAN	3	20
280	CAL	3	20
281	CAMELI	3	20
282	CARDAK	3	20
283	CIVRIL	3	20
284	GUNEY	3	20
285	HONAZ	3	20
286	KALE	3	20
287	MERKEZEFENDI	3	20
288	PAMUKKALE	3	20
289	SARAYKOY	3	20
290	SERINHISAR	3	20
291	TAVAS	3	20
292	BAGLAR	4	21
293	BISMIL	4	21
294	CERMIK	4	21
295	CINAR	4	21
296	CUNGUS	4	21
297	DICLE	4	21
298	EGIL	4	21
299	ERGANI	4	21
300	HANI	4	21
301	HAZRO	4	21
302	KAYAPINAR	4	21
303	KOCAKOY	4	21
304	KULP	4	21
305	LICE	4	21
306	SILVAN	4	21
307	SUR	4	21
308	YENISEHIR	4	21
309	AKCAKOCA	6	81
310	CUMAYERI	6	81
311	CILIMLI	6	81
312	GOLYAKA	6	81
313	GUMUSOVA	6	81
314	KAYNASLI	6	81
315	MERKEZ	6	81
316	YIGILCA	6	81
317	ENEZ	7	22
318	HAVSA	7	22
319	IPSALA	7	22
320	KESAN	7	22
321	LALAPASA	7	22
322	MERIC	7	22
323	MERKEZ	7	22
324	SULOGLU	7	22
325	UZUNKOPRU	7	22
326	AGIN	2	23
327	ALACAKAYA	2	23
328	ARICAK	2	23
329	BASKIL	2	23
330	KARAKOCAN	2	23
331	KEBAN	2	23
332	KOVANCILAR	2	23
333	MADEN	2	23
334	MERKEZ	2	23
335	PALU	2	23
336	SIVRICE	2	23
337	CAYIRLI	2	24
338	ILIC	2	24
339	KEMAH	2	24
340	KEMALIYE	2	24
341	MERKEZ	2	24
342	OTLUKBELI	2	24
343	REFAHIYE	2	24
344	TERCAN	2	24
345	UZUMLU	2	24
346	ASKALE	2	25
347	AZIZIYE	2	25
348	CAT	2	25
349	HINIS	2	25
350	HORASAN	2	25
351	ISPIR	2	25
352	KARACOBAN	2	25
353	KARAYAZI	2	25
354	KOPRUKOY	2	25
355	NARMAN	2	25
356	OLTU	2	25
357	OLUR	2	25
358	PALANDOKEN	2	25
359	PASINLER	2	25
360	PAZARYOLU	2	25
361	SENKAYA	2	25
362	TEKMAN	2	25
363	TORTUM	2	25
364	UZUNDERE	2	25
365	YAKUTIYE	2	25
366	ALPU	5	26
367	BEYLIKOVA	5	26
368	CIFTELER	5	26
369	GUNYUZU	5	26
370	HAN	5	26
371	INONU	5	26
372	MAHMUDIYE	5	26
373	MIHALGAZI	5	26
374	MIHALICCIK	5	26
375	ODUNPAZARI	5	26
376	SARICAKAYA	5	26
377	SEYITGAZI	5	26
378	SIVRIHISAR	5	26
379	TEPEBASI	5	26
380	ARABAN	4	27
381	ISLAHIYE	4	27
382	KARKAMIS	4	27
383	NIZIP	4	27
384	NURDAGI	4	27
385	OGUZELI	4	27
386	SAHINBEY	4	27
387	SEHITKAMIL	4	27
388	YAVUZELI	4	27
389	ALUCRA	6	28
390	BULANCAK	6	28
391	CAMOLUK	6	28
392	CANAKCI	6	28
393	DERELI	6	28
394	DOGANKENT	6	28
395	ESPIYE	6	28
396	EYNESIL	6	28
397	GORELE	6	28
398	GUCE	6	28
399	KESAP	6	28
400	MERKEZ	6	28
401	PIRAZIZ	6	28
402	SEBINKARAHISAR	6	28
403	TIREBOLU	6	28
404	YAGLIDERE	6	28
405	KELKIT	6	29
406	KOSE	6	29
407	KURTUN	6	29
408	MERKEZ	6	29
409	SIRAN	6	29
410	TORUL	6	29
411	CUKURCA	2	30
412	DERECIK	2	30
413	MERKEZ	2	30
414	SEMDINLI	2	30
415	YUKSEKOVA	2	30
416	ALTINOZU	1	31
417	ANTAKYA	1	31
418	ARSUZ	1	31
419	BELEN	1	31
420	DEFNE	1	31
421	DORTYOL	1	31
422	ERZIN	1	31
423	HASSA	1	31
424	ISKENDERUN	1	31
425	KIRIKHAN	1	31
426	KUMLU	1	31
427	PAYAS	1	31
428	REYHANLI	1	31
429	SAMANDAG	1	31
430	YAYLADAGI	1	31
431	ARALIK	2	76
432	KARAKOYUNLU	2	76
433	MERKEZ	2	76
434	TUZLUCA	2	76
435	AKSU	1	32
436	ATABEY	1	32
437	EGIRDIR	1	32
438	GELENDOST	1	32
439	GONEN	1	32
440	KECIBORLU	1	32
441	MERKEZ	1	32
442	SENIRKENT	1	32
443	SUTCULER	1	32
444	SARKIKARAAGAC	1	32
445	ULUBORLU	1	32
446	YALVAC	1	32
447	YENISARBADEMLI	1	32
448	ADALAR	7	34
449	ARNAVUTKOY	7	34
450	ATASEHIR	7	34
451	AVCILAR	7	34
452	BAGCILAR	7	34
453	BAHCELIEVLER	7	34
454	BAKIRKOY	7	34
455	BASAKSEHIR	7	34
456	BAYRAMPASA	7	34
457	BESIKTAS	7	34
458	BEYKOZ	7	34
459	BEYLIKDUZU	7	34
460	BEYOGLU	7	34
461	BUYUKCEKMECE	7	34
462	CATALCA	7	34
463	CEKMEKOY	7	34
464	ESENLER	7	34
465	ESENYURT	7	34
466	EYUPSULTAN	7	34
467	FATIH	7	34
468	GAZIOSMANPASA	7	34
469	GUNGOREN	7	34
470	KADIKOY	7	34
471	KAGITHANE	7	34
472	KARTAL	7	34
473	KUCUKCEKMECE	7	34
474	MALTEPE	7	34
475	PENDIK	7	34
476	SANCAKTEPE	7	34
477	SARIYER	7	34
478	SILIVRI	7	34
479	SULTANBEYLI	7	34
480	SULTANGAZI	7	34
481	SILE	7	34
482	SISLI	7	34
483	TUZLA	7	34
484	UMRANIYE	7	34
485	USKUDAR	7	34
486	ZEYTINBURNU	7	34
487	ALIAGA	3	35
488	BALCOVA	3	35
489	BAYINDIR	3	35
490	BAYRAKLI	3	35
491	BERGAMA	3	35
492	BEYDAG	3	35
493	BORNOVA	3	35
494	BUCA	3	35
495	CESME	3	35
496	CIGLI	3	35
497	DIKILI	3	35
498	FOCA	3	35
499	GAZIEMIR	3	35
500	GUZELBAHCE	3	35
501	KARABAGLAR	3	35
502	KARABURUN	3	35
503	KARSIYAKA	3	35
504	KEMALPASA	3	35
505	KINIK	3	35
506	KIRAZ	3	35
507	KONAK	3	35
508	MENDERES	3	35
509	MENEMEN	3	35
510	NARLIDERE	3	35
511	ODEMIS	3	35
512	SEFERIHISAR	3	35
513	SELCUK	3	35
514	TIRE	3	35
515	TORBALI	3	35
516	URLA	3	35
517	AFSIN	1	46
518	ANDIRIN	1	46
519	CAGLAYANCERIT	1	46
520	DULKADIROGLU	1	46
521	EKINOZU	1	46
522	ELBISTAN	1	46
523	GOKSUN	1	46
524	NURHAK	1	46
525	ONIKISUBAT	1	46
526	PAZARCIK	1	46
527	TURKOGLU	1	46
528	EFLANI	6	78
529	ESKIPAZAR	6	78
530	MERKEZ	6	78
531	OVACIK	6	78
532	SAFRANBOLU	6	78
533	YENICE	6	78
534	AYRANCI	5	70
535	BASYAYLA	5	70
536	ERMENEK	5	70
537	KAZIMKARABEKIR	5	70
538	MERKEZ	5	70
539	SARIVELILER	5	70
540	AKYAKA	2	36
541	ARPACAY	2	36
542	DIGOR	2	36
543	KAGIZMAN	2	36
544	MERKEZ	2	36
545	SARIKAMIS	2	36
546	SELIM	2	36
547	SUSUZ	2	36
548	ABANA	6	37
549	AGLI	6	37
550	ARAC	6	37
551	AZDAVAY	6	37
552	BOZKURT	6	37
553	CIDE	6	37
554	CATALZEYTIN	6	37
555	DADAY	6	37
556	DEVREKANI	6	37
557	DOGANYURT	6	37
558	HANONU	6	37
559	IHSANGAZI	6	37
560	INEBOLU	6	37
561	KURE	6	37
562	MERKEZ	6	37
563	PINARBASI	6	37
564	SEYDILER	6	37
565	SENPAZAR	6	37
566	TASKOPRU	6	37
567	TOSYA	6	37
568	AKKISLA	5	38
569	BUNYAN	5	38
570	DEVELI	5	38
571	FELAHIYE	5	38
572	HACILAR	5	38
573	INCESU	5	38
574	KOCASINAN	5	38
575	MELIKGAZI	5	38
576	OZVATAN	5	38
577	PINARBASI	5	38
578	SARIOGLAN	5	38
579	SARIZ	5	38
580	TALAS	5	38
581	TOMARZA	5	38
582	YAHYALI	5	38
583	YESILHISAR	5	38
584	BAHSILI	5	71
585	BALISEYH	5	71
586	CELEBI	5	71
587	DELICE	5	71
588	KARAKECILI	5	71
589	KESKIN	5	71
590	MERKEZ	5	71
591	SULAKYURT	5	71
592	YAHSIHAN	5	71
593	BABAESKI	7	39
594	DEMIRKOY	7	39
595	KOFCAZ	7	39
596	LULEBURGAZ	7	39
597	MERKEZ	7	39
598	PEHLIVANKOY	7	39
599	PINARHISAR	7	39
600	VIZE	7	39
601	AKCAKENT	5	40
602	AKPINAR	5	40
603	BOZTEPE	5	40
604	CICEKDAGI	5	40
605	KAMAN	5	40
606	MERKEZ	5	40
607	MUCUR	5	40
608	ELBEYLI	4	79
609	MERKEZ	4	79
610	MUSABEYLI	4	79
611	POLATELI	4	79
612	BASISKELE	7	41
613	CAYIROVA	7	41
614	DARICA	7	41
615	DERINCE	7	41
616	DILOVASI	7	41
617	GEBZE	7	41
618	GOLCUK	7	41
619	IZMIT	7	41
620	KANDIRA	7	41
621	KARAMURSEL	7	41
622	KARTEPE	7	41
623	KORFEZ	7	41
624	AHIRLI	5	42
625	AKOREN	5	42
626	AKSEHIR	5	42
627	ALTINEKIN	5	42
628	BEYSEHIR	5	42
629	BOZKIR	5	42
630	CIHANBEYLI	5	42
631	CELTIK	5	42
632	CUMRA	5	42
633	DERBENT	5	42
634	DEREBUCAK	5	42
635	DOGANHISAR	5	42
636	EMIRGAZI	5	42
637	EREGLI	5	42
638	GUNEYSINIR	5	42
639	HADIM	5	42
640	HALKAPINAR	5	42
641	HUYUK	5	42
642	ILGIN	5	42
643	KADINHANI	5	42
644	KARAPINAR	5	42
645	KARATAY	5	42
646	KULU	5	42
647	MERAM	5	42
648	SARAYONU	5	42
649	SELCUKLU	5	42
650	SEYDISEHIR	5	42
651	TASKENT	5	42
652	TUZLUKCU	5	42
653	YALIHUYUK	5	42
654	YUNAK	5	42
655	ALTINTAS	3	43
656	ASLANAPA	3	43
657	CAVDARHISAR	3	43
658	DOMANIC	3	43
659	DUMLUPINAR	3	43
660	EMET	3	43
661	GEDIZ	3	43
662	HISARCIK	3	43
663	MERKEZ	3	43
664	PAZARLAR	3	43
665	SIMAV	3	43
666	SAPHANE	3	43
667	TAVSANLI	3	43
668	AKCADAG	2	44
669	ARAPGIR	2	44
670	ARGUVAN	2	44
671	BATTALGAZI	2	44
672	DARENDE	2	44
673	DOGANSEHIR	2	44
674	DOGANYOL	2	44
675	HEKIMHAN	2	44
676	KALE	2	44
677	KULUNCAK	2	44
678	PUTURGE	2	44
679	YAZIHAN	2	44
680	YESILYURT	2	44
681	AHMETLI	3	45
682	AKHISAR	3	45
683	ALASEHIR	3	45
684	DEMIRCI	3	45
685	GOLMARMARA	3	45
686	GORDES	3	45
687	KIRKAGAC	3	45
688	KOPRUBASI	3	45
689	KULA	3	45
690	SALIHLI	3	45
691	SARIGOL	3	45
692	SARUHANLI	3	45
693	SELENDI	3	45
694	SOMA	3	45
695	SEHZADELER	3	45
696	TURGUTLU	3	45
697	YUNUSEMRE	3	45
698	ARTUKLU	4	47
699	DARGECIT	4	47
700	DERIK	4	47
701	KIZILTEPE	4	47
702	MAZIDAGI	4	47
703	MIDYAT	4	47
704	NUSAYBIN	4	47
705	OMERLI	4	47
706	SAVUR	4	47
707	YESILLI	4	47
708	AKDENIZ	1	33
709	ANAMUR	1	33
710	AYDINCIK	1	33
711	BOZYAZI	1	33
712	CAMLIYAYLA	1	33
713	ERDEMLI	1	33
714	GULNAR	1	33
715	MEZITLI	1	33
716	MUT	1	33
717	SILIFKE	1	33
718	TARSUS	1	33
719	TOROSLAR	1	33
720	YENISEHIR	1	33
721	BODRUM	3	48
722	DALAMAN	3	48
723	DATCA	3	48
724	FETHIYE	3	48
725	KAVAKLIDERE	3	48
726	KOYCEGIZ	3	48
727	MARMARIS	3	48
728	MENTESE	3	48
729	MILAS	3	48
730	ORTACA	3	48
731	SEYDIKEMER	3	48
732	ULA	3	48
733	YATAGAN	3	48
734	BULANIK	2	49
735	HASKOY	2	49
736	KORKUT	2	49
737	MALAZGIRT	2	49
738	MERKEZ	2	49
739	VARTO	2	49
740	ACIGOL	5	50
741	AVANOS	5	50
742	DERINKUYU	5	50
743	GULSEHIR	5	50
744	HACIBEKTAS	5	50
745	KOZAKLI	5	50
746	MERKEZ	5	50
747	URGUP	5	50
748	ALTUNHISAR	5	51
749	BOR	5	51
750	CAMARDI	5	51
751	CIFTLIK	5	51
752	MERKEZ	5	51
753	ULUKISLA	5	51
754	AKKUS	6	52
755	ALTINORDU	6	52
756	AYBASTI	6	52
757	CAMAS	6	52
758	CATALPINAR	6	52
759	CAYBASI	6	52
760	FATSA	6	52
761	GOLKOY	6	52
762	GULYALI	6	52
763	GURGENTEPE	6	52
764	IKIZCE	6	52
765	KABADUZ	6	52
766	KABATAS	6	52
767	KORGAN	6	52
768	KUMRU	6	52
769	MESUDIYE	6	52
770	PERSEMBE	6	52
771	ULUBEY	6	52
772	UNYE	6	52
773	BAHCE	1	80
774	DUZICI	1	80
775	HASANBEYLI	1	80
776	KADIRLI	1	80
777	MERKEZ	1	80
778	SUMBAS	1	80
779	TOPRAKKALE	1	80
780	ARDESEN	6	53
781	CAMLIHEMSIN	6	53
782	CAYELI	6	53
783	DEREPAZARI	6	53
784	FINDIKLI	6	53
785	GUNEYSU	6	53
786	HEMSIN	6	53
787	IKIZDERE	6	53
788	IYIDERE	6	53
789	KALKANDERE	6	53
790	MERKEZ	6	53
791	PAZAR	6	53
792	ADAPAZARI	7	54
793	AKYAZI	7	54
794	ARIFIYE	7	54
795	ERENLER	7	54
796	FERIZLI	7	54
797	GEYVE	7	54
798	HENDEK	7	54
799	KARAPURCEK	7	54
800	KARASU	7	54
801	KAYNARCA	7	54
802	KOCAALI	7	54
803	PAMUKOVA	7	54
804	SAPANCA	7	54
805	SERDIVAN	7	54
806	SOGUTLU	7	54
807	TARAKLI	7	54
808	19 MAYIS	6	55
809	ALACAM	6	55
810	ASARCIK	6	55
811	ATAKUM	6	55
812	AYVACIK	6	55
813	BAFRA	6	55
814	CANIK	6	55
815	CARSAMBA	6	55
816	HAVZA	6	55
817	ILKADIM	6	55
818	KAVAK	6	55
819	LADIK	6	55
820	SALIPAZARI	6	55
821	TEKKEKOY	6	55
822	TERME	6	55
823	VEZIRKOPRU	6	55
824	YAKAKENT	6	55
825	BAYKAN	4	56
826	ERUH	4	56
827	KURTALAN	4	56
828	MERKEZ	4	56
829	PERVARI	4	56
830	SIRVAN	4	56
831	TILLO	4	56
832	AYANCIK	6	57
833	BOYABAT	6	57
834	DIKMEN	6	57
835	DURAGAN	6	57
836	ERFELEK	6	57
837	GERZE	6	57
838	MERKEZ	6	57
839	SARAYDUZU	6	57
840	TURKELI	6	57
841	AKINCILAR	5	58
842	ALTINYAYLA	5	58
843	DIVRIGI	5	58
844	DOGANSAR	5	58
845	GEMEREK	5	58
846	GOLOVA	5	58
847	GURUN	5	58
848	HAFIK	5	58
849	IMRANLI	5	58
850	KANGAL	5	58
851	KOYULHISAR	5	58
852	MERKEZ	5	58
853	SUSEHRI	5	58
854	SARKISLA	5	58
855	ULAS	5	58
856	YILDIZELI	5	58
857	ZARA	5	58
858	AKCAKALE	4	63
859	BIRECIK	4	63
860	BOZOVA	4	63
861	CEYLANPINAR	4	63
862	EYYUBIYE	4	63
863	HALFETI	4	63
864	HALILIYE	4	63
865	HARRAN	4	63
866	HILVAN	4	63
867	KARAKOPRU	4	63
868	SIVEREK	4	63
869	SURUC	4	63
870	VIRANSEHIR	4	63
871	BEYTUSSEBAP	4	73
872	CIZRE	4	73
873	GUCLUKONAK	4	73
874	IDIL	4	73
875	MERKEZ	4	73
876	SILOPI	4	73
877	ULUDERE	4	73
878	CERKEZKOY	7	59
879	CORLU	7	59
880	ERGENE	7	59
881	HAYRABOLU	7	59
882	KAPAKLI	7	59
883	MALKARA	7	59
884	MARMARAEREGLISI	7	59
885	MURATLI	7	59
886	SARAY	7	59
887	SULEYMANPASA	7	59
888	SARKOY	7	59
889	ALMUS	6	60
890	ARTOVA	6	60
891	BASCIFTLIK	6	60
892	ERBAA	6	60
893	MERKEZ	6	60
894	NIKSAR	6	60
895	PAZAR	6	60
896	RESADIYE	6	60
897	SULUSARAY	6	60
898	TURHAL	6	60
899	YESILYURT	6	60
900	ZILE	6	60
901	AKCAABAT	6	61
902	ARAKLI	6	61
903	ARSIN	6	61
904	BESIKDUZU	6	61
905	CARSIBASI	6	61
906	CAYKARA	6	61
907	DERNEKPAZARI	6	61
908	DUZKOY	6	61
909	HAYRAT	6	61
910	KOPRUBASI	6	61
911	MACKA	6	61
912	OF	6	61
913	ORTAHISAR	6	61
914	SURMENE	6	61
915	SALPAZARI	6	61
916	TONYA	6	61
917	VAKFIKEBIR	6	61
918	YOMRA	6	61
919	CEMISGEZEK	2	62
920	HOZAT	2	62
921	MAZGIRT	2	62
922	MERKEZ	2	62
923	NAZIMIYE	2	62
924	OVACIK	2	62
925	PERTEK	2	62
926	PULUMUR	2	62
927	BANAZ	3	64
928	ESME	3	64
929	KARAHALLI	3	64
930	MERKEZ	3	64
931	SIVASLI	3	64
932	ULUBEY	3	64
933	BAHCESARAY	2	65
934	BASKALE	2	65
935	CALDIRAN	2	65
936	CATAK	2	65
937	EDREMIT	2	65
938	ERCIS	2	65
939	GEVAS	2	65
940	GURPINAR	2	65
941	IPEKYOLU	2	65
942	MURADIYE	2	65
943	OZALP	2	65
944	SARAY	2	65
945	TUSBA	2	65
946	ALTINOVA	7	77
947	ARMUTLU	7	77
948	CINARCIK	7	77
949	CIFTLIKKOY	7	77
950	MERKEZ	7	77
951	TERMAL	7	77
952	AKDAGMADENI	5	66
953	AYDINCIK	5	66
954	BOGAZLIYAN	5	66
955	CANDIR	5	66
956	CAYIRALAN	5	66
957	CEKEREK	5	66
958	KADISEHRI	5	66
959	MERKEZ	5	66
960	SARAYKENT	5	66
961	SARIKAYA	5	66
962	SORGUN	5	66
963	SEFAATLI	5	66
964	YENIFAKILI	5	66
965	YERKOY	5	66
966	ALAPLI	6	67
967	CAYCUMA	6	67
968	DEVREK	6	67
969	EREGLI	6	67
970	GOKCEBEY	6	67
971	KILIMLI	6	67
972	KOZLU	6	67
973	MERKEZ	6	67
\.


--
-- TOC entry 2198 (class 0 OID 0)
-- Dependencies: 178
-- Name: ilce_ilceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ilce_ilceid_seq', 1, false);


--
-- TOC entry 2142 (class 0 OID 24905)
-- Dependencies: 183
-- Data for Name: meyve; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.meyve (meyveid) FROM stdin;
\.


--
-- TOC entry 2199 (class 0 OID 0)
-- Dependencies: 182
-- Name: meyve_meyveid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.meyve_meyveid_seq', 1, false);


--
-- TOC entry 2144 (class 0 OID 24918)
-- Dependencies: 185
-- Data for Name: sebze; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sebze (sebzeid) FROM stdin;
\.


--
-- TOC entry 2200 (class 0 OID 0)
-- Dependencies: 184
-- Name: sebze_sebzeid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sebze_sebzeid_seq', 1, false);


--
-- TOC entry 2146 (class 0 OID 24931)
-- Dependencies: 187
-- Data for Name: tahil; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tahil (tahilid) FROM stdin;
\.


--
-- TOC entry 2201 (class 0 OID 0)
-- Dependencies: 186
-- Name: tahil_tahilid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tahil_tahilid_seq', 1, false);


--
-- TOC entry 2132 (class 0 OID 24866)
-- Dependencies: 173
-- Data for Name: ulke; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ulke (ulkename) FROM stdin;
\.


--
-- TOC entry 2140 (class 0 OID 24897)
-- Dependencies: 181
-- Data for Name: urun; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.urun (urunid, urunname, urunkatsayi) FROM stdin;
\.


--
-- TOC entry 2202 (class 0 OID 0)
-- Dependencies: 180
-- Name: urun_urunid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.urun_urunid_seq', 1, false);


--
-- TOC entry 2150 (class 0 OID 24957)
-- Dependencies: 191
-- Data for Name: veri; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.veri (veriid, toplamilacmiktari, toplammakinesayisi, iscisayisi, yil) FROM stdin;
\.


--
-- TOC entry 2203 (class 0 OID 0)
-- Dependencies: 190
-- Name: veri_veriid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.veri_veriid_seq', 1, false);


--
-- TOC entry 2156 (class 0 OID 25049)
-- Dependencies: 197
-- Data for Name: yetisir; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.yetisir (bolgeid, ilceid, ton, alan, yil) FROM stdin;
\.


--
-- TOC entry 2204 (class 0 OID 0)
-- Dependencies: 195
-- Name: yetisir_bolgeid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.yetisir_bolgeid_seq', 1, false);


--
-- TOC entry 2205 (class 0 OID 0)
-- Dependencies: 196
-- Name: yetisir_ilceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.yetisir_ilceid_seq', 1, false);


--
-- TOC entry 2159 (class 0 OID 25071)
-- Dependencies: 200
-- Data for Name: zitlasir; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.zitlasir (firsturunid, secondurunid) FROM stdin;
\.


--
-- TOC entry 2206 (class 0 OID 0)
-- Dependencies: 198
-- Name: zitlasir_firsturunid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.zitlasir_firsturunid_seq', 1, false);


--
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 199
-- Name: zitlasir_secondurunid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.zitlasir_secondurunid_seq', 1, false);


--
-- TOC entry 1997 (class 2606 OID 24949)
-- Name: bakliyat_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.bakliyat
    ADD CONSTRAINT bakliyat_pkey PRIMARY KEY (bakliyatid);


--
-- TOC entry 2001 (class 2606 OID 25013)
-- Name: barindirir_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.barindirir
    ADD CONSTRAINT barindirir_pkey PRIMARY KEY (ciftciid, ilceid);


--
-- TOC entry 1980 (class 2606 OID 24878)
-- Name: bolge_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.bolge
    ADD CONSTRAINT bolge_pkey PRIMARY KEY (bolgeid);


--
-- TOC entry 2007 (class 2606 OID 25098)
-- Name: bulundurur_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.bulundurur
    ADD CONSTRAINT bulundurur_pkey PRIMARY KEY (veriid, ilid);


--
-- TOC entry 1976 (class 2606 OID 24865)
-- Name: ciftci_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.ciftci
    ADD CONSTRAINT ciftci_pkey PRIMARY KEY (ciftciid);


--
-- TOC entry 1983 (class 2606 OID 24886)
-- Name: il_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.il
    ADD CONSTRAINT il_pkey PRIMARY KEY (ilid);


--
-- TOC entry 1987 (class 2606 OID 24894)
-- Name: ilce_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.ilce
    ADD CONSTRAINT ilce_pkey PRIMARY KEY (ilceid);


--
-- TOC entry 1991 (class 2606 OID 24910)
-- Name: meyve_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.meyve
    ADD CONSTRAINT meyve_pkey PRIMARY KEY (meyveid);


--
-- TOC entry 1993 (class 2606 OID 24923)
-- Name: sebze_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.sebze
    ADD CONSTRAINT sebze_pkey PRIMARY KEY (sebzeid);


--
-- TOC entry 1995 (class 2606 OID 24936)
-- Name: tahil_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.tahil
    ADD CONSTRAINT tahil_pkey PRIMARY KEY (tahilid);


--
-- TOC entry 1978 (class 2606 OID 24870)
-- Name: ulke_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.ulke
    ADD CONSTRAINT ulke_pkey PRIMARY KEY (ulkename);


--
-- TOC entry 1989 (class 2606 OID 24902)
-- Name: urun_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.urun
    ADD CONSTRAINT urun_pkey PRIMARY KEY (urunid);


--
-- TOC entry 1999 (class 2606 OID 24963)
-- Name: veri_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.veri
    ADD CONSTRAINT veri_pkey PRIMARY KEY (veriid);


--
-- TOC entry 2003 (class 2606 OID 25056)
-- Name: yetisir_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.yetisir
    ADD CONSTRAINT yetisir_pkey PRIMARY KEY (bolgeid, ilceid);


--
-- TOC entry 2005 (class 2606 OID 25077)
-- Name: zitlasir_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY public.zitlasir
    ADD CONSTRAINT zitlasir_pkey PRIMARY KEY (firsturunid, secondurunid);


--
-- TOC entry 1981 (class 1259 OID 25114)
-- Name: fki_bolge_fkey; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX fki_bolge_fkey ON public.il USING btree (bolgeid);


--
-- TOC entry 1984 (class 1259 OID 25125)
-- Name: fki_bolge_fkey2; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX fki_bolge_fkey2 ON public.ilce USING btree (bolgeid);


--
-- TOC entry 1985 (class 1259 OID 25131)
-- Name: fki_il_fkey2; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX fki_il_fkey2 ON public.ilce USING btree (ilid);


--
-- TOC entry 2014 (class 2606 OID 24950)
-- Name: bakliyat_bakliyatid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bakliyat
    ADD CONSTRAINT bakliyat_bakliyatid_fkey FOREIGN KEY (bakliyatid) REFERENCES public.urun(urunid);


--
-- TOC entry 2015 (class 2606 OID 25014)
-- Name: barindirir_ciftciid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.barindirir
    ADD CONSTRAINT barindirir_ciftciid_fkey FOREIGN KEY (ciftciid) REFERENCES public.ciftci(ciftciid);


--
-- TOC entry 2016 (class 2606 OID 25019)
-- Name: barindirir_ilceid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.barindirir
    ADD CONSTRAINT barindirir_ilceid_fkey FOREIGN KEY (ilceid) REFERENCES public.ilce(ilceid);


--
-- TOC entry 2008 (class 2606 OID 25109)
-- Name: bolge_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.il
    ADD CONSTRAINT bolge_fkey FOREIGN KEY (bolgeid) REFERENCES public.bolge(bolgeid);


--
-- TOC entry 2009 (class 2606 OID 25120)
-- Name: bolge_fkey2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ilce
    ADD CONSTRAINT bolge_fkey2 FOREIGN KEY (bolgeid) REFERENCES public.bolge(bolgeid);


--
-- TOC entry 2022 (class 2606 OID 25104)
-- Name: bulundurur_ilid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bulundurur
    ADD CONSTRAINT bulundurur_ilid_fkey FOREIGN KEY (ilid) REFERENCES public.il(ilid);


--
-- TOC entry 2021 (class 2606 OID 25099)
-- Name: bulundurur_veriid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bulundurur
    ADD CONSTRAINT bulundurur_veriid_fkey FOREIGN KEY (veriid) REFERENCES public.veri(veriid);


--
-- TOC entry 2010 (class 2606 OID 25126)
-- Name: il_fkey2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ilce
    ADD CONSTRAINT il_fkey2 FOREIGN KEY (ilid) REFERENCES public.il(ilid);


--
-- TOC entry 2011 (class 2606 OID 24911)
-- Name: meyve_meyveid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meyve
    ADD CONSTRAINT meyve_meyveid_fkey FOREIGN KEY (meyveid) REFERENCES public.urun(urunid);


--
-- TOC entry 2012 (class 2606 OID 24924)
-- Name: sebze_sebzeid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sebze
    ADD CONSTRAINT sebze_sebzeid_fkey FOREIGN KEY (sebzeid) REFERENCES public.urun(urunid);


--
-- TOC entry 2013 (class 2606 OID 24937)
-- Name: tahil_tahilid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tahil
    ADD CONSTRAINT tahil_tahilid_fkey FOREIGN KEY (tahilid) REFERENCES public.urun(urunid);


--
-- TOC entry 2017 (class 2606 OID 25057)
-- Name: yetisir_bolgeid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.yetisir
    ADD CONSTRAINT yetisir_bolgeid_fkey FOREIGN KEY (bolgeid) REFERENCES public.bolge(bolgeid);


--
-- TOC entry 2018 (class 2606 OID 25062)
-- Name: yetisir_ilceid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.yetisir
    ADD CONSTRAINT yetisir_ilceid_fkey FOREIGN KEY (ilceid) REFERENCES public.ilce(ilceid);


--
-- TOC entry 2019 (class 2606 OID 25078)
-- Name: zitlasir_firsturunid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.zitlasir
    ADD CONSTRAINT zitlasir_firsturunid_fkey FOREIGN KEY (firsturunid) REFERENCES public.urun(urunid);


--
-- TOC entry 2020 (class 2606 OID 25083)
-- Name: zitlasir_secondurunid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.zitlasir
    ADD CONSTRAINT zitlasir_secondurunid_fkey FOREIGN KEY (secondurunid) REFERENCES public.urun(urunid);


--
-- TOC entry 2170 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2020-12-05 21:42:51 +03

--
-- PostgreSQL database dump complete
--
