//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.7 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2020.04.19 at 10:20:30 PM CEST 
//


package com.project.xml.news;

import com.project.xml.types.File;

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
 *         &lt;element name="File" type="{http://www.project.com/xml/types}file"/>
 *       &lt;/sequence>
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
        "file"
})
@XmlRootElement(name = "StoreFileRequest")
public class StoreFileRequest {

    @XmlElement(name = "File", required = true)
    protected File file;

    /**
     * Gets the value of the file property.
     *
     * @return possible object is
     * {@link File }
     */
    public File getFile() {
        return file;
    }

    /**
     * Sets the value of the file property.
     *
     * @param value allowed object is
     *              {@link File }
     */
    public void setFile(File value) {
        this.file = value;
    }

}
