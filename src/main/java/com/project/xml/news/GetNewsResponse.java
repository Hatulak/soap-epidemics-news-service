//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.7 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2020.04.28 at 11:59:09 AM CEST 
//


package com.project.xml.news;

import com.project.xml.types.News;

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
 *         &lt;element name="News" type="{http://www.project.com/xml/types}news"/>
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
        "news"
})
@XmlRootElement(name = "GetNewsResponse")
public class GetNewsResponse {

    @XmlElement(name = "News", required = true)
    protected News news;

    /**
     * Gets the value of the news property.
     * 
     * @return
     *     possible object is
     *     {@link News }
     *     
     */
    public News getNews() {
        return news;
    }

    /**
     * Sets the value of the news property.
     * 
     * @param value
     *     allowed object is
     *     {@link News }
     *     
     */
    public void setNews(News value) {
        this.news = value;
    }

}
