//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.7 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2020.04.27 at 03:14:54 PM CEST 
//


package com.project.xml.news;

import javax.xml.bind.annotation.*;


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;sequence>
 *         &lt;element name="newsid" type="{http://www.w3.org/2001/XMLSchema}string"/>
 *       &lt;/sequence>
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 *
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
        "newsid"
})
@XmlRootElement(name = "GetNewsIdRequest")
public class GetNewsIdRequest {

    @XmlElement(required = true)
    protected String newsid;

    /**
     * Gets the value of the newsid property.
     *
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getNewsid() {
        return newsid;
    }

    /**
     * Sets the value of the newsid property.
     *
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setNewsid(String value) {
        this.newsid = value;
    }

}
