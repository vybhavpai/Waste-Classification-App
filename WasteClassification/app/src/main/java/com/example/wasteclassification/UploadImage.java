package com.example.wasteclassification;

public class UploadImage {
    private String mID;
    private String mCategory;
    private String mImageUrl;

    public UploadImage() {

    }

    public UploadImage(String ID, String Category, String imageUrl) {
        mID = ID;
        mCategory = Category;
        mImageUrl = imageUrl;
    }

    public String getmCategory() {
        return mCategory;
    }

    public void setmCategory(String mCategory) {
        this.mCategory = mCategory;
    }

    public String getmID() {
        return mID;
    }

    public void setmID(String mID) {
        this.mID = mID;
    }

    public String getmImageUrl() {
        return mImageUrl;
    }

    public void setmImageUrl(String mImageUrl) {
        this.mImageUrl = mImageUrl;
    }
}
